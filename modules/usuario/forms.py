from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.core.forms import form_abstract_password,form_abstract_confirm_password
from modules.usuario.validators import password_format_validator


class FormRegister(forms.Form):

    email = forms.EmailField(label="Email", max_length=256, required=False, error_messages=MENSAGENS_ERROS,
                             widget=forms.TextInput(
                                 attrs={'type': "text",
                                        'class': "form-control text-lowercase",
                                        'id': 'email',
                                        'ng-model': 'email',
                                        'autocomplete': "off",
                                        'placeholder': "Email..",
                                        'required':"true"
                                    }
                                )
                             )
    senha = forms.CharField(label="Senha", max_length=50, required=True, error_messages=MENSAGENS_ERROS,
                            widget=forms.TextInput(
                                attrs={'id': 'senha',
                                       'class': "form-control ",
                                       'type': "password",
                                       'autocomplete': "off",
                                       'ng-model': 'senha',
                                       'placeholder': "Senha..",
                                       'required': ""
                                    }
                                )
                            )

    confirma_senha = forms.CharField(label="Confirme a Senha", max_length=50, required=True,
                                     error_messages=MENSAGENS_ERROS,
                                     widget=forms.TextInput(
                                        attrs={'id': 'confirma_senha',
                                               'class': "form-control",
                                               'type': "password",
                                               'autocomplete': "off",
                                               'ng-model': 'confirma_senha',
                                               'placeholder': "Repita a Senha..",
                                               'required': ""
                                            }
                                        )
                                     )

    def clean(self):
        form_data = self.cleaned_data
        print ("VEJA O FORM DATA: ",form_data)
        if form_data['senha'] != form_data['confirma_senha']:
            self._errors["senha"] = ["Senha nao confere"]  # Will raise a error message
            del form_data['senha']
        return form_data


class FormLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=256, required=False, error_messages=MENSAGENS_ERROS,
                             widget=forms.TextInput(
                                 attrs={'type': "text",
                                        'class': "form-control text-lowercase",
                                        'id': 'email',
                                        'ng-model': 'email',
                                        'placeholder': "Email..",
                                        'required': "true"
                                        }
                                )
                             )
    senha = forms.CharField(label="Senha", max_length=50, required=True, error_messages=MENSAGENS_ERROS,
                            widget=forms.TextInput(
                                attrs={'id': 'senha',
                                       'class': "form-control ",
                                       'type': "password",
                                       'ng-model': 'senha',
                                       'placeholder': "Senha..",
                                       'required': ""
                                       }
                                )
                            )


class FormChangePassword(form_abstract_password, form_abstract_confirm_password):

    old_password = forms.CharField(
        label="Senha Antiga",
        max_length=50,
        required=True,
        validators=[password_format_validator],
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'id': 'old_password', 'class': "form-control",'type': "password",'autocomplete': "off", 'ng-model': 'old_password',
                'required': "required", 'data-validate-length-range': '8', 'pattern': '(\d+[a-zA-Z]+)|([a-zA-Z]+\d+)'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(form_abstract_password, self).__init__(*args, **kwargs)
        super(form_abstract_confirm_password, self).__init__(*args, **kwargs)
        self.fields['password'].label = "Nova Senha"
