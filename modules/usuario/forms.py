from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.core.forms import FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail
from modules.usuario.validators import password_format_validator


class FormConfRegister(FormAbstractEmail):

    chave = forms.CharField(label="Registro", max_length=200, required=True, error_messages=MENSAGENS_ERROS,
                            widget=forms.TextInput(
                                attrs={'id': 'chave',
                                       'class': "form-control ",
                                       'type': "text",
                                       'autocomplete': "off",
                                       'ng-model': 'chave',
                                       'placeholder': "Registro..",
                                       'required': "False"
                                    }
                                )
                            )

    def __init__(self, *args, **kwargs):
        super(FormAbstractEmail, self).__init__(*args,**kwargs)

    '''A def clean tem q conferir se a chava digitada é igual a recebida no email'''


class FormResetPassword(FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractEmail, self).__init__(*args,**kwargs)


class FormActivationCode(forms.Form):

    activation_code = forms.CharField(
        label="Chave de Ativação",
        max_length=46,
        required=False,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'activation_code', 'class': "form-control",'readonly': True,'ng-model': 'activation_code',
                'required': "required", 'data-validate-length-range': '46'
            }
        )
    )


class FormLogin(FormAbstractEmail, FormAbstractPassword):

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractEmail, self).__init__(*args,**kwargs)


class FormChangePassword(FormAbstractPassword, FormAbstractConfirmPassword):

    old_password = forms.CharField(
        label="Senha Antiga",
        max_length=50,
        required=True,
        validators=[password_format_validator],
        error_messages=MENSAGENS_ERROS,
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
        errors = str(self.errors)
        for item in self.fields:
            errors = errors.replace("<li>" + str(item), "<li>" + self.fields[item].label)
        return errors


class FormRegister(FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractConfirmPassword, self).__init__(*args, **kwargs)
        super(FormAbstractEmail, self).__init__(*args,**kwargs)

    def clean(self):
        form_data = self.cleaned_data
        if len(self.cleaned_data) == len(self.fields):
            if form_data['password'] != form_data['confirm_password']:
                self._errors["password"] = ["Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                del form_data['password']
        return form_data
