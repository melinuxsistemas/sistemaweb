from django.db import models
from modules.core.config import ERRORS_MESSAGES
from modules.entity.validators import cpf_cnpj_validator, min_words_name_validator, birthdate_validator


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

    entity_type = models.CharField("Tipo de Entidade:", max_length=2, null=False, default='PF', choices=options_type_entity, error_messages=ERRORS_MESSAGES)
    cpf_cnpj = models.CharField("CPF ou CNPJ", max_length=32, unique=True, null=False, validators=[cpf_cnpj_validator], error_messages=ERRORS_MESSAGES)
    entity_name = models.CharField("Nome ou Razão Social", null=False, max_length=64,validators=[min_words_name_validator], error_messages=ERRORS_MESSAGES)
    fantasy_name = models.CharField("Nome Fantasia", max_length=32, error_messages=ERRORS_MESSAGES)
    birth_date_foundation = models.DateTimeField("Data de Nascimento ou Fundação", null=True, blank=True, validators=[birthdate_validator], error_messages=ERRORS_MESSAGES)
    relations_company = models.CharField("Tipo de Relação Empresarial", null=True, blank=True, max_length=512, error_messages=ERRORS_MESSAGES)
    company_activities = models.CharField("Atividade Comercial", null=True, blank=True, max_length=512, error_messages=ERRORS_MESSAGES)
    market_segments = models.CharField("Segmento de Mercado",max_length=512,null=True,blank=True)
    registration_status = models.IntegerField(choices=options_registration_status, default=0, error_messages=ERRORS_MESSAGES)
    comments = models.TextField("Observações",max_length=500,null=True, blank=True)
    created_date = models.DateField(auto_now_add=True,null=True)
    last_update = models.DateField(null=True,auto_now=True)
    history = models.CharField("Histórico de Alterações",max_length=500)

    def __unicode__(self):
        return self.cpf_cnpj

class Contact (models.Model,BaseModel):

    id_contact = models.AutoField(primary_key=True)
    id_entity = models.ForeignKey(Entity,  null=False,on_delete=models.CASCADE,  error_messages=ERRORS_MESSAGES )
    type_contact = models.CharField("Tipo de Contato",max_length=10,  error_messages=ERRORS_MESSAGES)
    name = models.CharField("Nome", max_length=30, null=False, error_messages=ERRORS_MESSAGES)
    ddd = models.CharField("DDD", max_length=4, null=False, blank=False,  error_messages=ERRORS_MESSAGES)
    phone = models.CharField("Numero de telefone", max_length=10, null=False, blank=False,  error_messages=ERRORS_MESSAGES)
    operadora = models.CharField("Operadora Telefonica", max_length=10, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    details = models.CharField("Detalhes",max_length=10, error_messages=ERRORS_MESSAGES)
    history = models.CharField("Histórico de Alterações", max_length=500)