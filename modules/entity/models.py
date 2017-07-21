from django.db import models
from modules.core.config import MENSAGENS_ERROS


class Entidade:

    options_type_entity = (
        (0,"Pessoa Física"),
        (1,"Pessoa Jurídica"),
        (2,"Órgão Público"),
        (3,"Estrangeiro"),
        (4,"Estraneiro Pessoa Jurídica")
    )
    options_registration_status = (
        (0,'Habilitado'),
        (1,'bloqueado'),
        (2,'Desabilitado'),
        (9,'Falecido/Encerrou Atividade')
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

    type_entity             = models.PositiveIntegerField("Tipo de Entidade:", max_length=1,null=False,choices=options_type_entity, error_messages=MENSAGENS_ERROS)
    cpf_cnpj                = models.CharField           ("CPF/CNPJ",max_length=32, unique=True,validators=[], error_messages=MENSAGENS_ERROS)
    entity_name             = models.CharField           ("Nome/Razão",max_length=64,error_messages=MENSAGENS_ERROS)
    fantasy_name            = models.CharField           ("Nome Fantasia",max_length=32,error_messages=MENSAGENS_ERROS)
    birth_date_foundation   = models.DateTimeField       ("Data de Nascimento/Fundação",validators=[],error_messages=MENSAGENS_ERROS)
    relation_company        = models.PositiveIntegerField("Tipo de Relação",choices=options_relation_company,null=True,blank=True,error_messages=MENSAGENS_ERROS)
    company_activities      = models.PositiveIntegerField("Atividade Comercial:",choices=options_activities,null=True,blank=True,error_messages=MENSAGENS_ERROS)
    market_segment          = models.CharField           ("Segmento de Mercado",max_length=20,null=True,blank=True)
    registration_status     = models.PositiveIntegerField(choices=options_registration_status,default='0',error_messages=MENSAGENS_ERROS)
    comments                = models.TextField           ("Observações",max_length=500,null=True, blank=True)
    create_date             = models.DateField           (auto_now_add=True,null=True)
    last_update             = models.DateField           (null=True,auto_now=True)
    history                 = models.CharField           ("Historico de atualizações")