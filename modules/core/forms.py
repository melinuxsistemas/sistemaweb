from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.usuario.validators import email_dangerous_symbols_validator, password_format_validator


class form_abstract_password(forms.Form):
    password = forms.CharField(
        label="Senha",
        max_length=50,
        required=True,
        validators=[password_format_validator],
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'password','name': 'password', 'class': "form-control ", 'type': "password",
                'autocomplete': "off", 'ng-model': 'password','required': "required",
                'data-validate-length-range': '8', 'pattern': '(\d+[a-zA-Z]+)|([a-zA-Z]+\d+)'
            }
        )
    )

class form_abstract_confirm_password(forms.Form):
    confirm_password = forms.CharField(
        label="Confirme a Senha",
        max_length=50,
        required=True, validators=[password_format_validator],
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'confirm_password','name':'confir_password', 'class': "form-control", 'type': "password",
                'autocomplete': "off",'ng-model': 'confirm_password','required': "required",
                'data-validate-length-range': '8', 'pattern': '(\d+[a-zA-Z]+)|([a-zA-Z]+\d+)','data-validate-linked':'password'
            }
        )
    )

    def clean_confirm_password(self):
        password = self.clean_data.get('password', '')
        password_repeat = self.clean_data.get('confirm_password', '')

        if password != password_repeat:
            raise forms.ValidationError("The passwords don't match.")


class form_abstract_email(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=256,
        required=False,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'type': "text", 'class': "form-control text-lowercase", 'id': 'email',
                'ng-model': 'email', 'autocomplete': "off", 'placeholder': "Email..",'required': "true"
            }
        )
    )