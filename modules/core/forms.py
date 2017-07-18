from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.user.validators import email_dangerous_symbols_validator, password_format_validator, email_format_validator


class FormAbstractEmail(forms.Form):

    email = forms.EmailField(
        label="Email",
        max_length=256,
        required=True,
        validators=[email_format_validator, email_dangerous_symbols_validator],
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'type': "text", 'class': "form-control text-lowercase", 'id': 'email',
                'ng-model': 'email', 'autocomplete': "off", 'placeholder': "",'required': "true"
            }
        )
    )


class FormAbstractPassword(forms.Form):
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
                'data-validate-length-range': '8',
            }
        )
    )


class FormAbstractConfirmPassword(forms.Form):
    confirm_password = forms.CharField(
        label="Confirme a Senha",
        max_length=50,
        required=True, validators=[password_format_validator],
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'confirm_password','name':'confirm_password', 'class': "form-control", 'type': "password",
                'autocomplete': "off",'ng-model': 'confirm_password','required': "required",
                'data-validate-length-range': '8', 'pattern': '(\d+[a-zA-Z]+)|([a-zA-Z]+\d+)','data-validate-linked':'password'
            }
        )
    )

class FormAbstractEntity (forms.Form):
    cpf_cnpj = forms.CharField("CPF/CNPJ", max_length=14, unique=True, validators=[], error_messages=MENSAGENS_ERROS)
    nome_razao = forms.CharField("Nome/Razão", max_length=50, error_messages=MENSAGENS_ERROS)
    nome_fantasia = forms.CharField("Nome Fantasia", max_length=25, error_messages=MENSAGENS_ERROS)
    data_nasc_fund = forms.DateTimeField("Data de Nascimento/Fundação", validators=[], error_messages=MENSAGENS_ERROS)
    tipo_entidade = forms.PositiveIntegerField("Tipo de Entidade:", max_length=1, null=False, error_messages=MENSAGENS_ERROS)
    tipo_relacao = forms.CharField("Tipo de Relação", max_length=4, null=True, blank=True,
                                    error_messages=MENSAGENS_ERROS)
    natureza_juridica = forms.CharField("Natureza Juridica", max_length=4, null=True, blank=True, validators=[],
                                         error_messages=MENSAGENS_ERROS)
    atividade = forms.CharField("Atividade:", max_length=2, null=True, blank=True, error_messages=MENSAGENS_ERROS)
    segmento_mercado = forms.CharField("Segmento de Mercado", max_length=20, null=True, blank=True)
    obs_tributaria_NF = forms.CharField("Observações Tributarias na Nota Fiscal", max_length=128, null=True,
                                         blank=True)
    situacao_cadastro = forms.CharField( default='0', error_messages=MENSAGENS_ERROS)
    observacoes = forms.TextField("Observações", null=True, blank=True)
    detalhes = forms.CharField(null=True, blank=True)