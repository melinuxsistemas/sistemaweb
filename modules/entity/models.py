from django.db import models
from modules.core.config import ERRORS_MESSAGES
from modules.entity.validators import cpf_cnpj_validator, min_words_name_validator, future_birthdate_validator, maximum_age_person_validator, minimum_age_person_validator, \
    required_validator
from django.core.validators import MinLengthValidator


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


class Entity(models.Model,BaseModel):

    class Meta:
        db_table = 'entity'
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    options_type_entity = (
        ("PF","Pessoa Física"),
        ("PJ","Pessoa Jurídica"),
        ("OP","Órgão Público"),
        ("PX","Pessoa Estrangeiro"),
        ("EX","Empresa Estraneira")
    )
    options_registration_status = (
        (0,'Habilitado'),
        (1,'Bloqueado'),
        (2,'Desabilitado'),
        (9,'Falecido / Encerrou Atividade')
    )
    options_relation_company = (
        (0, "Cliente"),
        (1, "Fornecedor"),
        (2, "Funcionário"),
        (3, "Transportador"),
        (4, "Banco"),
        (5, "Representante")
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

    model_exceptions = []

    entity_type = models.CharField("Tipo de Entidade:", max_length=2, null=False, default='PF', choices=options_type_entity, error_messages=ERRORS_MESSAGES)
    cpf_cnpj = models.CharField("CPF ou CNPJ", max_length=32, unique=True, null=False, validators=[cpf_cnpj_validator,required_validator], error_messages=ERRORS_MESSAGES)
    entity_name = models.CharField("Nome ou Razão Social", null=False, blank=False, max_length=64,validators=[min_words_name_validator,MinLengthValidator(1)], error_messages=ERRORS_MESSAGES)
    fantasy_name = models.CharField("Nome Fantasia", max_length=32, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    birth_date_foundation = models.DateField("Data de Nascimento ou Fundação", null=True, blank=True, validators=[future_birthdate_validator, minimum_age_person_validator, maximum_age_person_validator], error_messages=ERRORS_MESSAGES)
    relations_company = models.CharField("Tipo de Relação Empresarial", null=True, blank=True, max_length=512, error_messages=ERRORS_MESSAGES)
    company_activities = models.CharField("Atividade Comercial", null=True, blank=True, max_length=512, error_messages=ERRORS_MESSAGES)
    market_segments = models.CharField("Segmento de Mercado",max_length=512,null=True,blank=True)
    registration_status = models.IntegerField(choices=options_registration_status, default=0, error_messages=ERRORS_MESSAGES)
    comments = models.TextField("Observações",max_length=500,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    last_update = models.DateTimeField(null=True,auto_now=True)
    history = models.CharField("Histórico de Alterações",max_length=500,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.model_exceptions = self.check_validators()
        if self.model_exceptions == []:
            super(Entity, self).save(*args, **kwargs)
        else:
            raise self.model_exceptions[0]

    def check_validators(self):
        self.model_exceptions = []
        if self.entity_type == "PF":
            try:
                cpf_cnpj_validator(self.cpf_cnpj)
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
                cpf_cnpj_validator(self.cpf_cnpj)
            except Exception as e:
                self.model_exceptions.append(e)
        return self.model_exceptions

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

    def __unicode__(self):
        return self.cpf_cnpj