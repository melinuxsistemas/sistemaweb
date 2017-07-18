from django import forms
from modules.core.config import MENSAGENS_ERROS

class FormEntity (forms.Form):

    options_entity_type = (
        (0, "Pessoa Física"),
        (1, "Pessoa Jurídica"),
        (2, "Órgão Público")
    )

    options_relation_type = (
        (0, "Cliente"),
        (1, "Fornecedor"),
        (2, "Funcionário"),
        (3, "Transportador"),
        (4, "Banco"),
        (5, "Representante")
    )

    options_activity = (
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

    options_status_register = (
        (0, "Habilitado"),
        (1, "Bloqueado"),
        (2, "Desabilitado"),
        (9, "Falecido/Encerrou Atividade"),
    )
    tipo_entidade = forms.ChoiceField(
        label="Tipo de Entidade:",
        choices= options_entity_type,
        max_length=1,
        null=False,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs= {
                'id': 'tipo_entidade','name': 'tipo_entidade', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'tipo_entidade','required': "required",
            }
        )
    )

    cpf_cnpj = forms.CharField(
        label="CPF/CNPJ",
        max_length=14,
        unique=True, validators=[],required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'cpf_cnpj','name': 'cpf_cnpj', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'cpf_cnpj','required': "required"
            }
        )
    )

    nome_razao = forms.CharField(
        label="Nome/Razão",
        max_length=50,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'nome_razao', 'name': 'nome_razao', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'nome_razao', 'required': "required",
            }
        )
    )

    nome_fantasia = forms.CharField(
        label="Nome Fantasia",
        max_length=25,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'nome_fantasia','name': 'nome_fantasia', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'nome_fantasia','required': "required",
            }
        )
    )

    nascimento_fundacao = forms.DateTimeField(
        label="Nascimento/Fundação",
        error_messages=MENSAGENS_ERROS,
        required=True,
        validators=[],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs= {
                'id': 'nascimento_fundacao', 'name': 'nascimento_fundacao', 'class': "form-control ", 'type': "datetime",
                'ng-model': 'nascimento_fundacao', 'required': "required",
            }
        )
    )


    relation_type = forms.MultipleChoiceField(
        label="Tipo de Relação",
        max_length=4,
        choices= options_relation_type,
        null=True,
        blank=True,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs={
                'id': 'relation_type', 'name': 'relation_type', 'class': "form-control ",
                'autocomplete': "off", 'ng-model': 'relation_type',
            }
        )
    )

    activity = forms.MultipleChoiceField(
        label="Atividade:",
        max_length=2,
        choices=options_activity,
        null=True,
        blank=True,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs={
                'id': 'activity','name': 'activity', 'activity': "form-control ", 'ng-model': 'activity'
            }
        )
    )

    natureza_juridica = forms.CharField(
        label="Natureza Juridica",
        max_length=4,
        null=True,
        blank=True,
        validators=[],
        error_messages=MENSAGENS_ERROS,
        widget= forms.TextInput(
            attrs={
                'id': 'natureza_juridica','name': 'natureza_juridica', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'natureza_juridica','required': "required"
            }
        )
    )

    segmento_mercado = forms.CharField(
        label="Segmento de Mercado",
        max_length=20,
        null=True,
        blank=True
    )

    obs_tributaria_NF = forms.CharField(
        label="Observações Tributarias na Nota Fiscal",
        max_length=128,
        null=True,
        blank=True,
        widget= forms.TextInput(
            attrs={
                'id': 'obs_tributaria_NF','name': 'obs_tributaria_NF', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'obs_tributaria_NF'
            }
        )
    )

    registration_status = forms.ChoiceField(
        default='0',
        choices= options_status_register,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs={
                'id': 'registration_status','name': 'registration_status', 'class': "form-control ", 'type': "text",'ng-model': 'registration_status',
            }
        )

    )

    observations = forms.CharField(
        label="Observações",
        null=True,
        blank=True,
        widget=forms.TextInput(
            attrs={
                'id': 'observations','name': 'observations', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'observations',
            }
        )
    )

    detalhes = forms.CharField(
        null=True,
        blank=True,
        widget = forms.TextInput(
            attrs={
                'id': 'detalhes','name': 'detalhes', 'class': "form-control ",'hidden':'true', 'type': "detalhes",
                'autocomplete': "off", 'ng-model': 'detalhes',
            }
        )
    )


    def __init__(self):
        super().__init__()
        self.fields['tipo_entidade'] = "Tipo Entidade.."
        self.fields['cpf_cnpj'].widget.attrs['placeholder'] = 'CPF/CNPJ..'
        self.fields['nome_razao'].widget.attrs['placeholder'] = 'Nome ou Razao..'
        self.fields['nome_fantasia'].widget.attrs['placeholder'] = 'Nome Fantasia..'
        self.fields['data_nasc_fund'] = "Data Nascimento/Fundação.."
