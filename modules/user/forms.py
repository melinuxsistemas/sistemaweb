from django import forms
from modules.core.config import ERRORS_MESSAGES
from modules.core.forms import FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail
from modules.entity.models import Entity
from modules.user.validators import password_format_validator


class FormLogin(FormAbstractEmail, FormAbstractPassword):

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractEmail, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email..'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha..'


class FormRegister(FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractConfirmPassword, self).__init__(*args, **kwargs)
        super(FormAbstractEmail, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email..'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha..'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Repita a Senha..'

    def clean(self):
        form_data = self.cleaned_data
        if len(self.cleaned_data) == len(self.fields):
            if form_data['password'] != form_data['confirm_password']:
                self._errors["password"] = ["Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                del form_data['password']
        return form_data


class FormConfirmRegister(FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractEmail, self).__init__(*args,**kwargs)
        self.fields['email'].widget.input_type = 'hidden'


class FormResetPassword(FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractEmail, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Informe seu Email..'


class FormChangePassword(FormAbstractPassword, FormAbstractConfirmPassword):

    old_password = forms.CharField(
        label="Senha Antiga",
        max_length=50,
        required=True,
        validators=[password_format_validator],
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'old_password', 'class': "form-control",'type': "password",'autocomplete': "off", 'ng-model': 'old_password',
                'required': "required", 'data-validate-length-range': '8', 'ng-pattern': '(\d+[a-zA-Z]+)|([a-zA-Z]+\d+)'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractConfirmPassword, self).__init__(*args, **kwargs)
        self.fields['password'].label = "Nova Senha"

    def clean(self):
        form_data = self.cleaned_data
        if len(self.cleaned_data) == len(self.fields):
            if form_data['password'] != form_data['confirm_password']:
                self._errors["password"] = ["Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                del form_data['password']

            elif form_data['old_password'] == form_data['password']:
                self._errors["password"] = ["Nova Senha: Precisa ser diferente da senha antiga."]  # Will raise a error message
                del form_data['password']
        return form_data

    def format_validate_response(self):
        response_errors = {}
        #print("VEJA OS ERROS: ",self.errors.as_data)
        if self.errors:
            errors = self.errors
            for campo in errors:
                response_errors[campo] = []
                for erro in errors[campo]:
                    erro_format = str(erro)
                    erro_format = erro_format.replace("['","")
                    erro_format = erro_format.replace("']", "")
                    response_errors[campo].append(erro_format)
            print(response_errors)
        else:
            print("TEM NADA DE ERRO EU AXO")
        return response_errors


class FormActivationCode(forms.Form):

    activation_code = forms.CharField(
        label="Código de Ativação",
        max_length=46,
        required=False,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'activation_code',
                'class': "form-control",
                'readonly': True,
                'ng-model': 'activation_code',
                'required': "required",
                'data-validate-length-range': '46'
            }
        )
    )

class FormAutonomy (forms.Form):
    access_level = (
        ("0", "Sem Acesso"),
        ("1", "vizualizar"),
        ("2", "adicionar"),
        ("3", "alterar"),
        # ... Ainda possui mais
    )

    id_company = forms.CharField(
        label="Empresa",
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'id_company',
                'class': "form-control",
                'ng-model': 'id_company',
                'required': True,
            }
        )
    )

    id_user = forms.ModelChoiceField(
        queryset= Entity.objects.filter(entity_type='PF').values('entity_name'),
        label="Funcionário",
        empty_label='Selecione um funcionário',
        required=True,
        widget=forms.Select(
            attrs={
                'id': 'id_user',
                'class': "form-control",
                'name':'entity_name',
                'ng-model': 'id_user',
                'required': True,
            }
        )
    )


    menu_01 = forms.MultipleChoiceField(
        label="Entidades",
        choices=access_level,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'Entidades',
                'class': "form-control",
                'ng-model': 'Entidades',
            }
        )
    )

    menu_02 = forms.MultipleChoiceField(
        label="Menu 02",
        choices=access_level,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'id': 'menu_02',
                'class': "form-control",
                'ng-model': 'menu_02'
            }
        )
    )