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

    type_entity = forms.MultipleChoiceField(
        label="Tipo de Entidade:",
        choices= options_entity_type,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs= {
                'id': 'tipo_entidade','name': 'tipo_entidade', 'class': "form-control ",
                'ng-model': 'tipo_entidade','required': "required",
            }
        )
    )

    cpf_cnpj = forms.CharField(
        label="CPF/CNPJ",
        max_length=32,
        validators=[],
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'cpf_cnpj','name': 'cpf_cnpj', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'cpf_cnpj','required': "required"
            }
        )
    )

    entity_name = forms.CharField(
        label="Nome/Razão",
        max_length=64,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'nome_razao', 'name': 'nome_razao', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'nome_razao', 'required': "required",
            }
        )
    )

    fantasy_name = forms.CharField(
        label="Nome Fantasia",
        max_length=32,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'nome_fantasia','name': 'nome_fantasia', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'nome_fantasia','required': "required",
            }
        )
    )

    birth_date_foundation = forms.DateTimeField(
        label="Nascimento/Fundação",
        error_messages=MENSAGENS_ERROS,
        required=True,
        validators=[],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs= {
                'id': 'nascimento_fundacao', 'name': 'nascimento_fundacao', 'class': "form-control ", 'type':'date',
                'ng-model': 'nascimento_fundacao', 'required': "required",
            }
        )
    )

    relation_company = forms.MultipleChoiceField(
        label="Tipo de Relação",
        choices= options_relation_type,
        error_messages=MENSAGENS_ERROS,
        widget= forms.CheckboxSelectMultiple(
            attrs= {'id':'relation_type', 'class':'form-contro', 'name':'relation_type', 'ng-model' : 'relation_type'}
        )
    )

    company_activities = forms.MultipleChoiceField(
        label="Atividade:",
        choices=options_activity,
        error_messages=MENSAGENS_ERROS,
        widget= forms.CheckboxSelectMultiple(
            attrs={'id': 'activity', 'class': 'form-contro', 'name': 'activity', 'ng-model': 'activity'}
        )
    )

    market_segment = forms.CharField(
        label="Segmento de Mercado",
        max_length=20,
        widget= forms.TextInput(
            attrs= {
                'id': 'segmento_mercado', 'name':'segmento_mercado','class':'form-control', 'type':'text',
                'ng-model':'segmento_mercado'
            }
        )

    )

    registration_status = forms.ChoiceField(
        choices= options_status_register,
        error_messages=MENSAGENS_ERROS,
        widget= forms.Select(
            attrs={
                'id': 'registration_status','name': 'registration_status', 'class': "form-control ",
                'type': "text",'ng-model': 'registration_status','hidden':'true'
            }
        )

    )

    comments = forms.CharField(
        label="Observações",
        max_length= 500,

        widget=forms.Textarea(
            attrs={
                'id': 'observations', 'name': 'observations', 'class': "form-control ", 'cols':2,'rows':3,
                'type': "text", 'ng-model': 'observations'
            }
        )
    )

    history = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'detalhes','name': 'detalhes', 'class': "form-control ",'hidden':'true', 'type': "detalhes",
                'autocomplete': "off", 'ng-model': 'detalhes',
            }
        )
    )


    def __init__(self, *args, **kwargs):
        super(FormEntity,self).__init__(*args, **kwargs)
        self.fields['cpf_cnpj'].widget.attrs['placeholder']             = 'CPF/CNPJ..'
        self.fields['entity_name'].widget.attrs['placeholder']          = 'Nome ou Razao..'
        self.fields['fantasy_name'].widget.attrs['placeholder']         = 'Nome Fantasia..'
        self.fields['birth_date_foundation'].widget.attrs['plaseholder']= "Data Nascimento/Fundação.."
        self.fields['market_segment'].widget.attrs['placeholder']       = "Segmento Mercado"
        self.fields['comments'].widget.attrs['placeholder']             = 'Obervações'
        self.fields['registration_status'].widget                       = forms.HiddenInput()
