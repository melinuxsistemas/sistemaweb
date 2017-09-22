from django import forms
from modules.core.config import ERRORS_MESSAGES
from modules.core.forms import FormAbstractEmail
from modules.entity.validators import cpf_cnpj_validator, future_birthdate_validator, min_words_name_validator


class AbstractFormEntity (forms.Form):

    options_entity_type = (
        (0, "Pessoa Física"),
        (1, "Pessoa Jurídica"),
        (2, "Órgão Público")
    )

    options_status_register = (
        (0, "Habilitado"),
        (1, "Bloqueado"),
        (2, "Desabilitado"),
        (9, "Falecido/Encerrou Atividade"),
    )

    entity_type = forms.CharField(
        label="Tipo",
        max_length=2,
        validators=[],
        required=True,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'entity_type', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_type', 'required': "required"
            }
        )
    )

    cpf_cnpj = forms.CharField(
        label="CPF",
        max_length=32,
        #validators=[cpf_cnpj_validator],
        required=True,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'cpf_cnpj', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'cpf_cnpj'
            }
        )
    )

    entity_name = forms.CharField(
        label="Nome Completo",
        max_length=64,
        required=True,
        #validators=[min_words_name_validator],
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'entity_name', 'name': 'entity_name', 'class': "form-control uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_name', 'required': "True", #'pattern':'\S[a-z,A-Z]{2} \S[a-z,A-Z]{2}',
                'data-validate-length-range': '6'
            }
        )
    )

    fantasy_name = forms.CharField(
        label="Nome Fantasia",
        max_length=32,
        required=False,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'fantasy_name', 'class': "form-control optional uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'fantasy_name', 'data-validate-length-range': '3' #retirar o tamanho, colocado pra test
            }
        )
    )

    birth_date_foundation = forms.DateTimeField(
        label="Data de Nascimento",
        error_messages=ERRORS_MESSAGES,
        required=False,
        #validators=[future_birthdate_validator],
        widget=forms.TextInput(
            attrs= {
                'id': 'birth_date_foundation', 'class': "form-control optional", 'type':'text',
                'ng-model': 'birth_date_foundation'
            }
        )
    )

    registration_status = forms.ChoiceField(
        choices=options_status_register,
        error_messages=ERRORS_MESSAGES,
        required=False,
        initial=0,
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
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'observations', 'name': 'observations', 'class': "form-control uppercase", 'cols':2,'rows':3,
                'type': "text", 'ng-model': 'observations'
            }
        )
    )

    history = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                'id': 'detalhes','name': 'detalhes', 'class': "form-control ",'hidden':'true', 'type': "detalhes",
                'autocomplete': "off", 'ng-model': 'detalhes',
            }
        )
    )

    def format_validate_response(self):
        response_errors = {}
        if self.errors:
            errors = self.errors
            for campo in errors:
                response_errors[campo] = []
                for erro in errors[campo]:
                    erro_format = str(erro)
                    erro_format = erro_format.replace("['", "")
                    erro_format = erro_format.replace("']", "")
                    response_errors[campo].append(erro_format)
        return response_errors


class FormPersonEntity(AbstractFormEntity):
    def __init__(self, *args, **kwargs):
        super(AbstractFormEntity, self).__init__(*args, **kwargs)
        #self.fields['cpf_cnpj'].label = "CPF"
        #self.fields['entity_name'].label = 'Nome Completo'
        #self.fields['fantasy_name'].label = 'Apelido'
        #self.fields['birth_date_foundation'].label = "Data de Nascimento"

    def clean(self):
        form_data = self.cleaned_data
        """
        if len(self.cleaned_data) == len(self.fields):
            if form_data['password'] != form_data['confirm_password']:
                self._errors["password"] = [
                    "Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                del form_data['password']

            elif form_data['old_password'] == form_data['password']:
                self._errors["password"] = [
                    "Nova Senha: Precisa ser diferente da senha antiga."]  # Will raise a error message
                del form_data['password']
        """
        return form_data


class FormCompanyEntity(AbstractFormEntity):
    options_relation_type = (
        (0, "Cliente"), (1, "Fornecedor"),
        (2, "Funcionário"), (3, "Transportador"),
        (4, "Banco"), (5, "Representante")
    )

    options_activity = (
        (0, "Consumidor"), (1, "Comércio"), (2, "Serviços"),
        (3, "Indústria"), (4, "Transporte"), (5, "Importação"),
        (6, "Exportação"), (7, "Produtor Rural"), (8, "Extrativista"),)

    relations_company = forms.MultipleChoiceField(label="Tipo de Relação", choices=options_relation_type,
                                                  error_messages=ERRORS_MESSAGES, widget=forms.CheckboxSelectMultiple(
            attrs={'id': 'relation_type', 'class': 'form-control', 'name': 'relation_type',
                   'ng-model': 'relation_type'}))

    company_activities = forms.MultipleChoiceField(label="Tipo de Atividade Empresarial", choices=options_activity,
                                                   error_messages=ERRORS_MESSAGES, widget=forms.CheckboxSelectMultiple(
            attrs={'id': 'activity', 'class': 'form-contro', 'name': 'activity', 'ng-model': 'activity'}))

    market_segment = forms.CharField(label="Segmento de Mercado", max_length=20, widget=forms.TextInput(
        attrs={'id': 'market_segment', 'class': 'form-control', 'type': 'text', 'ng-model': 'market_segment',
            'list': 'options_segments'}))

    def __init__(self, *args, **kwargs):
        super(AbstractFormEntity, self).__init__(*args, **kwargs)
        self.fields['cpf_cnpj'].label = "CNPJ"
        self.fields['entity_name'].label = 'Razão Social'
        self.fields['fantasy_name'].label = 'Nome Fantasia'
        self.fields['birth_date_foundation'].label = "Data de Fundação"

    """
    #def __init__(self, *args, **kwargs):
        super(AbstractFormEntity, self).__init__(*args, **kwargs)

        self.fields['cpf_cnpj'].widget.attrs['placeholder']             = 'CPF/CNPJ..'
        self.fields['entity_name'].widget.attrs['placeholder']          = 'Nome ou Razao..'
        self.fields['fantasy_name'].widget.attrs['placeholder']         = 'Nome Fantasia..'
        self.fields['birth_date_foundation'].widget.attrs['plaseholder']= "Data Nascimento/Fundação.."
        self.fields['market_segment'].widget.attrs['placeholder']       = "Segmento Mercado"
        self.fields['comments'].widget.attrs['placeholder']             = 'Obervações'
        self.fields['registration_status'].widget                       = forms.HiddenInput()
    """

class FormRegisterPhone (FormAbstractEmail):
    def clean(self):
        form_data = self.cleaned_data
        print("Olha o clean Phone",form_data)
        return  form_data

    type_contact = forms.CharField(
        label="Tipo de contato",
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id':'type_contact', 'name': 'type_contact', 'class': 'form-control'
            }
        )
    )

    name = forms.CharField(
        label="Nome Completo",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'name_contact', 'name': 'name_contact', 'class': 'form-control'
            }
        )
    )

    ddd = forms.CharField(
        label="DDD",
        max_length=4,
        widget= forms.TextInput(
            attrs={
                'id':'ddd','name':'ddd','class':'form-control'
            }
        )
    )

    phone = forms.CharField(
        label="Telefone",
        max_length=10,
        widget= forms.TextInput(
            attrs={
                'id':'phone_number','name':'phone_number','class':'form-control'
            }
        )
    )

    operadora = forms.CharField(
        label="Operadora",
        max_length=10,
        widget= forms.TextInput(
            attrs={
                'id':'operadora', 'name':'operadora', 'class':'form-control'
            }
        )
    )

    comments = forms.CharField(
        label="Observações",
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'observations', 'name': 'observations', 'class': "form-control uppercase", 'cols': 2, 'rows': 3,
                'type': "text", 'ng-model': 'observations'
            }
        )
    )

    history = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'detalhes', 'name': 'detalhes', 'class': "form-control ", 'hidden': 'true', 'type': "detalhes",
                'autocomplete': "off", 'ng-model': 'detalhes',
            }
        )
    )

class FormRegisterEmailEntity (FormAbstractEmail):

    boolean_email = (
        (True,'SIM'),
        (False,'Não')
    )

    def __init__(self, *args, **kwargs):
        super(FormAbstractEmail, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email..'

    name = forms.CharField(
        label="Nome Completo",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'name', 'name': 'name', 'class': 'form-control', 'ng-model': 'name', 'placeholder':'Nome..'
                ,'autocomplete': 'off' , 'type': "text"
            }
        )
    )

    send_xml = forms.ChoiceField(
        label="Enviar XML",
        choices= boolean_email,
        widget= forms.Select(
            attrs= {
                'id': 'send_xml', 'name':'send_xml','class':'form_control'
            }
        )
    )#models.BooleanField("Envia XML", null=False, blank=False, error_messages=ERRORS_MESSAGES)

    send_suitcase = forms.ChoiceField(
        label="Enviar Mala",
        choices=boolean_email,
        widget=forms.Select(
            attrs={
                'id': 'send_suitcase', 'name': 'send_suitcase', 'class': 'send_suitcase'
            }
        )
    )

    comments = forms.CharField(
        label="Observações",
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'observations', 'name': 'observations', 'class': "form-control uppercase", 'cols': 2, 'rows': 3,
                'type': "text", 'ng-model': 'observations'
            }
        )
    )

    history = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'detalhes', 'name': 'detalhes', 'class': "form-control ", 'hidden': 'true', 'type': "detalhes",
                'autocomplete': "off", 'ng-model': 'detalhes',
            }
        )
    )
