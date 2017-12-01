from django.db import models
from modules.core.config import ERRORS_MESSAGES
from modules.entity.validators import cpf_cnpj_validator, min_words_name_validator, future_birthdate_validator, maximum_age_person_validator, minimum_age_person_validator, required_validator, only_numeric, validate_ddd
from django.core.validators import MinLengthValidator
from modules.user.validators import email_format_validator, email_dangerous_symbols_validator


class BaseModel:

    def show_fields_value(self):
        for k, v in [(x, getattr(self, x)) for x in self.__dict__ if not x.startswith('_')]:
            print(k,":",v)

    def form_to_object(self, form):
        for attribute, value in [(x, getattr(self, x)) for x in self.__dict__ if not x.startswith('_')]:
            try:
                form_value = form.cleaned_data[attribute]
                setattr(self,attribute,form_value)
            except:
                pass


class Entity(models.Model, BaseModel):

    class Meta:
        db_table = 'entity'
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    options_type_entity = (
        ('1',"Pessoa Física"),
        ('2',"Pessoa Jurídica"),
        ('3',"Órgão Público"),
        ('4',"Pessoa Estrangeiro"),
        ('5',"Empresa Estraneira")
    )
    options_registration_status = (
        (0,'Habilitado'),
        (1,'Bloqueado'),
        (2,'Desabilitado'),
        (9,'Falecido / Encerrou Atividade')
    )
    options_relation_company = (
        ('0', "Cliente"),
        ('1', "Fornecedor"),
        ('2', "Funcionário"),
        ('3', "Transportador"),
        ('4', "Representante"),
        ('5', "Banco")

    )
    options_activities = (
        (0, "Consumidor"),
        (1, "Comércio"),
        (2, "Serviços"),
        (3, "Indústria"),
        (4, "Transporte"),
        (5, "Importação"),
        (6, "Exportação"),
        (7, "Produtor Rural"),
        (8, "Extrativista"),
    )

    entity_type = models.CharField("Tipo de Entidade:", max_length=2, null=False, choices=options_type_entity, error_messages=ERRORS_MESSAGES)
    cpf_cnpj = models.CharField("CPF ou CNPJ", max_length=32, unique=True, null=False, validators=[cpf_cnpj_validator,required_validator], error_messages=ERRORS_MESSAGES)
    entity_name = models.CharField("Nome ou Razão Social", null=False, blank=False, max_length=64,validators=[min_words_name_validator,MinLengthValidator(1)], error_messages=ERRORS_MESSAGES)
    fantasy_name = models.CharField("Nome Fantasia", max_length=32, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    birth_date_foundation = models.DateField("Data de Nascimento ou Fundação", null=True, blank=True, validators=[future_birthdate_validator, minimum_age_person_validator, maximum_age_person_validator], error_messages=ERRORS_MESSAGES)
    natureza_juridica = models.ForeignKey('core.NaturezaJuridica',null=True, blank=True) #models.CharField("Tipo de Relação", null=True, blank=True, max_length=64, error_messages=ERRORS_MESSAGES)
    main_activity = models.ForeignKey('core.EconomicActivity',null=True, blank=True)
    relations_company = models.CharField("Tipo de Relação", max_length=50, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    registration_status = models.IntegerField(choices=options_registration_status, default=0, error_messages=ERRORS_MESSAGES)
    comments = models.TextField("Observações",max_length=500,null=True, blank=True)
    comments_fiscal_note = models.TextField("Observações para Nota Fiscal",max_length=512,null=True, blank=True)

    # Complemento para pessoas Juridica
    company_activities = models.CharField("Atividade Comercial", null=True, blank=True, max_length=512, error_messages=ERRORS_MESSAGES)
    market_segments = models.CharField("Segmento de Mercado",null=True,max_length=512,blank=True, error_messages=ERRORS_MESSAGES)
    tributary_regime = models.CharField("Regime Tributário",null=True,max_length=512,blank=True, error_messages=ERRORS_MESSAGES)
    buy_destination = models.CharField("Destino da Compra",null=True,max_length=512,blank=True, error_messages=ERRORS_MESSAGES)

    # Complemento para pessoa Fisica
    entity_father = models.CharField("Nome Completo do Pai", null=True, blank=True, max_length=64, error_messages=ERRORS_MESSAGES)
    entity_mother = models.CharField("Nome Completo da Mãe", null=True, blank=True, max_length=64, error_messages=ERRORS_MESSAGES)
    entity_conjuge = models.CharField("Nome Completo do Conjuge", null=True, blank=True, max_length=64, error_messages=ERRORS_MESSAGES)
    entity_occupation = models.CharField("Profissão", null=True, blank=True, max_length=64, error_messages=ERRORS_MESSAGES)

    # Informacoes de Controle
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    last_update = models.DateTimeField(auto_now=True, null=False)
    history = models.CharField("Histórico de Alterações", max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        print("ENTRANDO NO FULL CLEAN")
        self.full_clean()
        super(Entity, self).save(*args, **kwargs)

    """
    def check_validators(self):
        self.model_exceptions = []
        if self.entity_type == "PF":
            try:
                cpf_validator(self.cpf_cnpj)
            except Exception as e:
                self.model_exceptions.append(e)

            try:
                minimum_age_person_validator(self.birth_date_foundation)
            except Exception as e:
                self.model_exceptions.append(e)

            try:
                maximum_age_person_validator(self.birth_date_foundation)
            except Exception as e:
                self.model_exceptions.append(e)

            try:
                future_birthdate_validator(self.birth_date_foundation)
            except Exception as e:
                self.model_exceptions.append(e)
        else:
            try:
                cnpj_validator(self.cpf_cnpj)
            except Exception as e:
                self.model_exceptions.append(e)
        return self.model_exceptions
    """


    """
    def clean(self):
        print("ENTREI NO CLEAN CARAI..")
        form_data = self.cleaned_data
        if len(self.cleaned_data) == len(self.fields):
            print("OLHA TODOS CAMPOS ESTAO LIMPOS INDIVIDUALMENTE")

            if(form_data['entity_type'] == 'PF'):
                print("VEJA A DATA: ",form_data['birth_date_foundation'],type(form_data['birth_date_foundation']))

            elif(form_data['entity_type'] == 'PF'):
                print("EH EMPRESA, ENTAO O NASCIMENTO PODE SER RECENTE E NAO TEM LIMITE DE IDADE")

            else:
                print("SE NAO EH PF OU PJ NAO FAZ NADA...")
                ""
                value = 
                current_date = datetime.datetime.now().date()
                print("VEJA A DATA QUE VEIO: ", value)
                print("VEJA A DATA QUE PEGUEI: ", current_date)
                if value > current_date:
                    raise ValidationError(_("Date can not be future"), code='future_date')
                    return False
                return True

                if form_data['password'] != form_data['confirm_password']:
                    self._errors["password"] = ["Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                    del form_data['password']
                ""
        else:
            print("ALGUM CAMPO JA DEU ERRO INDIVIDUALMENTE")
        return form_data
        """
    def delete(self, using=None, keep_parents=False):
        self.desativar()

    def desativar (self):
        print("Consegui deletar???")
        self.registration_status = 2

    def __unicode__(self):
        return self.cpf_cnpj


class Contact(models.Model,BaseModel):

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    models_exceptions = []

    options_type_contact = (
        (1, "CELULAR"),
        (2, "FIXO"),
        (3, "SAC"),
        (4, "FAX")
    )

    id = models.AutoField(primary_key=True, unique=True)
    entity = models.ForeignKey(to=Entity,on_delete=models.CASCADE,null=False,error_messages=ERRORS_MESSAGES)
    type_contact = models.IntegerField(choices=options_type_contact,null=False ,default=1, error_messages=ERRORS_MESSAGES)
    name = models.CharField("Nome", max_length=30, null=False, error_messages=ERRORS_MESSAGES)
    ddd = models.CharField("DDD", max_length=4,validators=[only_numeric], null=False, blank=False,  error_messages=ERRORS_MESSAGES)
    phone = models.CharField("Numero de telefone",validators=[only_numeric],max_length=10, error_messages=ERRORS_MESSAGES)
    complemento = models.CharField("Complemento", max_length=32, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    details = models.CharField("Detalhes",max_length=10,null=True,blank=True, error_messages=ERRORS_MESSAGES)
    history = models.CharField("Histórico de Alterações",null=True,blank=True, max_length=500)

    def save(self, *args, **kwargs):
        self.model_exceptions = self.check_validators()
        if self.model_exceptions == []:
            try:
                super(Contact, self).save(*args, **kwargs)
            except Exception as exception:
                self.model_exceptions.append(exception)
                raise exception
        else:
            raise self.model_exceptions[0]

    def check_validators(self):
        self.model_exceptions = []

        try:
            only_numeric(self.phone)
        except Exception as e:
            self.model_exceptions.append(e)

        try:
            only_numeric(self.ddd)
        except Exception as e:
            self.model_exceptions.append(e)
        try:
            validate_ddd(self.ddd, self.type_contact)
        except Exception as e:
            self.model_exceptions.append(e)
        return self.model_exceptions

    def desativar (self):
        self.delete()


class Email (models.Model, BaseModel):


    class Meta:
        db_table = 'email'
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField(('Email'), null=False,blank=False, max_length=255, validators=[email_format_validator, email_dangerous_symbols_validator], error_messages=ERRORS_MESSAGES)
    name = models.CharField("Nome", max_length=30, null=False,blank=False, error_messages=ERRORS_MESSAGES)
    entity = models.ForeignKey(to=Entity, on_delete=models.CASCADE, null=False,blank=False, error_messages=ERRORS_MESSAGES)
    send_xml = models.BooleanField("Envia XML", null=False,blank=False,error_messages=ERRORS_MESSAGES)
    send_suitcase = models.BooleanField("Envia Mala",null=False,blank=False, error_messages=ERRORS_MESSAGES)
    details = models.CharField("Detalhes", max_length=10, null= True, blank= True, error_messages=ERRORS_MESSAGES)
    history = models.CharField("Histórico de Alterações", null= True, blank= True, max_length=500,error_messages=ERRORS_MESSAGES)

    model_exceptions = []

    def save(self, *args, **kwargs):
        self.model_exceptions = self.check_validators()
        if self.model_exceptions == []:
            try:
                super(Email, self).save(*args, **kwargs)
            except Exception as exception:
                self.model_exceptions.append(exception)
                raise exception
        else:
            raise self.model_exceptions[0]

    def check_validators(self):
        self.model_exceptions = []

        try:
            email_format_validator(self.email)
        except Exception as e:
            self.model_exceptions.append(e)

        try:
            email_dangerous_symbols_validator(self.email)
        except Exception as e:
            self.model_exceptions.append(e)
        return self.model_exceptions

    def desativar (self):
        self.delete()