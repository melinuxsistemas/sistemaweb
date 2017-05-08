from django import forms
from modules.usuario.models import Usuario
from modules.core.config import MENSAGENS_ERROS


class formulario_register(forms.Form):

    email = forms.EmailField(label="Email", max_length=256, required=False, error_messages=MENSAGENS_ERROS,
                             widget=forms.TextInput(
                                 attrs={'type': "text",
                                        'class': "form-control text-lowercase",
                                        'id': 'email',
                                        'ng-model': 'email',
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
                                               'ng-model': 'confirma_senha',
                                               'placeholder': "Senha..",
                                               'required': ""
                                            }
                                        )
                                     )

    def clean(self):
        form_data = self.cleaned_data
        if form_data['senha'] != form_data['confirma_senha']:
            self._errors["senha"] = ["Senha nao confere"]  # Will raise a error message
            del form_data['senha']
        return form_data
