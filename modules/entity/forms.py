from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.entity.validators import cpf_cnpj_validator


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

    cpf_cnpj = forms.CharField(
        label="CPF",
        max_length=32,
        validators=[cpf_cnpj_validator],
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
        label="Nome Completo",
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
        required=False,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'fantasy_name', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'fantasy_name'
            }
        )
    )

    birth_date_foundation = forms.DateTimeField(
        label="Data de Nascimento",
        error_messages=MENSAGENS_ERROS,
        required=False,
        validators=[],
        widget=forms.TextInput(
            attrs= {
                'id': 'birth_date_foundation', 'class': "form-control ", 'type':'text',
                'ng-model': 'birth_date_foundation'
            }
        )
    )

    registration_status = forms.ChoiceField(
        choices=options_status_register,
        error_messages=MENSAGENS_ERROS,
        required=False,
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
                'id': 'observations', 'name': 'observations', 'class': "form-control ", 'cols':2,'rows':3,
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
        # print("VEJA OS ERROS: ",self.errors.as_data)
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
        error_messages=MENSAGENS_ERROS, widget=forms.CheckboxSelectMultiple(
            attrs={'id': 'relation_type', 'class': 'form-contro', 'name': 'relation_type',
                   'ng-model': 'relation_type'}))

    company_activities = forms.MultipleChoiceField(label="Tipo de Atividade Empresarial", choices=options_activity,
        error_messages=MENSAGENS_ERROS, widget=forms.CheckboxSelectMultiple(
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