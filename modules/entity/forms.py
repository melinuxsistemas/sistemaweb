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
                'id': 'type_entity','name': 'type_entity', 'class': "form-control ",
                'ng-model': 'type_entity','required': "required",
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
                'id': 'entity_name', 'name': 'entity_name', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_name', 'required': "required",
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
                'id': 'fantasy_name','name': 'fantasy_name', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'fantasy_name','required': "required",
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
                'id': 'birth_date_foundation', 'name': 'birth_date_foundation', 'class': "form-control ", 'type':'date',
                'ng-model': 'birth_date_foundation', 'required': "required",
            }
        )
    )

    relation_company = forms.MultipleChoiceField(
        label="Tipo de Relação",
        choices= options_relation_type,
        error_messages=MENSAGENS_ERROS,
        widget= forms.CheckboxSelectMultiple(
            attrs= {'id':'relation_company', 'class':'form-contro', 'name':'relation_company', 'ng-model' : 'relation_company'}
        )
    )

    company_activities = forms.MultipleChoiceField(
        label="Atividade",
        choices=options_activity,
        error_messages=MENSAGENS_ERROS,
        widget= forms.SelectMultiple(
            attrs={'id': 'company_activities','incline': True, 'multiple':'multiple','class': 'form-control', 'name': 'company_activities', 'ng-model': 'company_activities'}
        )
    )

    market_segment = forms.CharField(
        label="Segmento de Mercado",
        max_length=20,
        widget= forms.TextInput(
            attrs= {
                'id': 'market_segment', 'name':'market_segment','class':'form-control', 'type':'text',
                'ng-model':'market_segment'
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
                'id': 'comments', 'name': 'comments', 'class': "form-control ", 'cols':2,'rows':3,
                'type': "text", 'ng-model': 'comments'
            }
        )
    )

    history = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'history','name': 'history', 'class': "form-control ",'hidden':'true',
                'autocomplete': "off", 'ng-model': 'history',
            }
        )
    )


    def __init__(self, *args, **kwargs):
        super(FormEntity,self).__init__(*args, **kwargs)
        self.fields['registration_status'].widget = forms.HiddenInput()
