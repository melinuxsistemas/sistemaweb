from django import forms
from modules.core.config import MENSAGENS_ERROS
from modules.core.forms import FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail
from modules.usuario.validators import password_format_validator


class FormRegister(FormAbstractPassword,FormAbstractConfirmPassword,FormAbstractEmail):

    def __init__(self, *args, **kwargs):
        super(FormAbstractPassword, self).__init__(*args, **kwargs)
        super(FormAbstractConfirmPassword, self).__init__(*args, **kwargs)
        super(FormAbstractEmail, self).__init__(*args,**kwargs)

    def clean(self):
        data = self.data
        form_data = self.cleaned_data
        #print('form data', len(form_data), form_data)
        #print('data', len(data), data)
        if len(form_data) < len(data):
            #print("criar limpador de form")
            pass
            '''limpar campos e deletar form igual esta na outra'''

        return form_data



    '''def clean(self):
        form_data = self.data
        print("Valore recebidos:    ", self.data)
        print('erros->', self.errors)
        print('formulario',form_data)
        if form_data['password'] != form_data['confirm_password']:
            self._errors["password"] = ["Senha nao confere"]  # Will raise a error message
            form_data = self.cleaned_data
            del form_data['password']
        return form_data'''


    '''email = forms.EmailField(
        label="Email", max_length=256, required=False, error_messages=MENSAGENS_ERROS,
            widget=forms.TextInput(
                attrs={
                    'type': "text",
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
                                     )'''


class FormConfRegister(forms.Form):

    email = forms.EmailField(label="Email", max_length=256, required=True, error_messages=MENSAGENS_ERROS,
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

class FormResetPassword(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=256,
        required=True,
        error_messages=MENSAGENS_ERROS,
        widget=forms.TextInput(
            attrs={
                'type': "email",
                'class': "form-control text-lowercase",
                'id': 'email',
                'ng-model': 'email',
                'placeholder': "Email..",
                'required': "True"
                }
            )
        )


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


[
'__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
    '__html__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'as_data', 'as_json',
    'as_text', 'as_ul', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
    'setdefault', 'update', 'values']