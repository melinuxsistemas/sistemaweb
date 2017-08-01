from django.db import models
from modules.core.config import MENSAGENS_ERROS
from modules.entity.validators import cpf_cnpj_validator


class Entity(models.Model):

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

    type_entity = models.CharField("Tipo de Entidade:", max_length=2,null=False,choices=options_type_entity, error_messages=MENSAGENS_ERROS)
    cpf_cnpj = models.CharField("CPF ou CNPJ",max_length=32, unique=True,null=False,validators=[cpf_cnpj_validator], error_messages=MENSAGENS_ERROS)
    entity_name = models.CharField("Nome ou Razão Social",null=False,max_length=64,error_messages=MENSAGENS_ERROS)
    fantasy_name = models.CharField("Nome Fantasia",null=False,max_length=32,error_messages=MENSAGENS_ERROS)
    birth_date_foundation = models.DateTimeField("Data de Nascimento ou Fundação",null=True,blank=True,validators=[],error_messages=MENSAGENS_ERROS)
    relations_company = models.CharField("Tipo de Relação Empresarial",null=True,blank=True,max_length=512,error_messages=MENSAGENS_ERROS)
    company_activities = models.CharField("Atividade Comercial",null=True,blank=True,max_length=512,error_messages=MENSAGENS_ERROS)
    market_segments = models.CharField("Segmento de Mercado",max_length=512,null=True,blank=True)
    registration_status = models.IntegerField(choices=options_registration_status,default=0,error_messages=MENSAGENS_ERROS)
    comments = models.TextField("Observações",max_length=500,null=True, blank=True)
    created_date = models.DateField(auto_now_add=True,null=True)
    last_update = models.DateField(null=True,auto_now=True)
    history = models.CharField("Histórico de Alterações",max_length=500)


