from django.db import models
from modules.core.config import MENSAGENS_ERROS


class Entidade ():

    opcoes_tipos_entidade = (
        (0,"Pessoa Física"),
        (1,"Pessoa Jurídica"),
        (2,"Órgão Público")
    )

    opcoes_situacao_cadastro = (
        ('0','Habilitado'),
        ('1','bloqueado'),
        ('2','Desabilitado'),
        ('9','Falecido/Encerrou Atividade')
    )

    cpf_cnpj           = models.CharField           ("CPF/CNPJ",max_length=14, unique=True,validators=[], error_messages=MENSAGENS_ERROS)
    nome_razao         = models.CharField           ("Nome/Razão",max_length=50,error_messages=MENSAGENS_ERROS)
    nome_fantasia      = models.CharField           ("Nome Fantasia",max_length=25,error_messages=MENSAGENS_ERROS)
    data_nasc_fund     = models.DateTimeField       ("Data de Nascimento/Fundação",validators=[],error_messages=MENSAGENS_ERROS)
    tipo_entidade      = models.PositiveIntegerField("Tipo de Entidade:",max_length=1,null=False,choices=opcoes_tipos_entidade,error_messages=MENSAGENS_ERROS)
    tipo_relacao       = models.CharField           ("Tipo de Relação",max_length=4,null=True,blank=True,error_messages=MENSAGENS_ERROS)
    natureza_juridica  = models.CharField           ("Natureza Juridica",max_length=4,null=True,blank=True,validators=[],error_messages=MENSAGENS_ERROS)
    atividade          = models.CharField           ("Atividade:",max_length=2,null=True,blank=True,error_messages=MENSAGENS_ERROS)
    segmento_mercado   = models.CharField           ("Segmento de Mercado",max_length=20,null=True,blank=True)
    obs_tributaria_NF  = models.CharField           ("Observações Tributarias na Nota Fiscal",max_length=128,null=True,blank=True)
    situacao_cadastro  = models.CharField           (choices=opcoes_situacao_cadastro,default='0',error_messages=MENSAGENS_ERROS)
    observacoes        = models.TextField           ("Observações",null=True, blank=True)
    detalhes           = models.CharField           (null=True,blank=True)