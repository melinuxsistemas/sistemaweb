from django import forms

from libs.default.core import BaseForm
from modules.core.config import ERRORS_MESSAGES
from modules.core.forms import FormAbstractEmail
from modules.core.models import EconomicActivity, NaturezaJuridica, MarketSegment
from modules.entity.models import BaseModel, Contact, Email
from modules.entity.models import Entity
from modules.entity.validators import cpf_cnpj_validator, future_birthdate_validator, min_words_name_validator
from sistemaweb import settings


class EntityIdentificationForm(forms.Form, BaseForm):

    model = Entity

    options_entity_type = (
        ('1', "PESSOA FÍSICA"),
        ('2', "PESSOA JURÍDICA"),
        ('3', "ÓRGÃO PÚBLICO")
    )

    options_status_register = (
        (0, "Habilitado"),
        (1, "Bloqueado"),
        (2, "Desabilitado"),
        (9, "Falecido/Encerrou Atividade"),
    )

    entity_type = forms.ChoiceField(label='Tipo',choices=options_entity_type,required=True,
        error_messages=ERRORS_MESSAGES,
        widget=forms.Select(
            attrs={
                'id': 'entity_type', 'class': "selectpicker form-control",
                'ng-model': 'entity_type', 'required': "required", 'title':'', 'selectOnTab':True,'onchange':'select_entity_type()'
            }
        )
    )

    cpf_cnpj = forms.CharField(label="CPF",max_length=32,validators=[cpf_cnpj_validator],required=True,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'cpf_cnpj', 'class': "form-control ", 'type': "text",
                'autocomplete': "off", 'ng-model': 'cpf_cnpj', 'required':'required'
            }
        )
    )

    entity_name = forms.CharField(label="Nome Completo",max_length=64,required=True,validators=[min_words_name_validator],
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'entity_name', 'name': 'entity_name', 'class': "form-control uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_name', 'required': 'required', #'pattern':'\S[a-z,A-Z]{2} \S[a-z,A-Z]{2}',
                'data-validate-length-range': '6'
            }
        )
    )

    fantasy_name = forms.CharField(
        label="Nome Fantasia",max_length=32,required=False,
        error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'fantasy_name', 'class': "form-control optional uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'fantasy_name', 'data-validate-length-range': '3' #retirar o tamanho, colocado pra test
            }
        )
    )

    birth_date_foundation = forms.DateField(
        label="Data de Nascimento",required=False,validators=[future_birthdate_validator],
        error_messages=ERRORS_MESSAGES,
        widget=forms.DateInput(
            attrs= {
                'id': 'birth_date_foundation', 'class': "form-control optional", 'type':'text',
                'ng-model': 'birth_date_foundation',
            }
        )
    )

    natureza_juridica = forms.ModelChoiceField(label='Natureza Jurídica', queryset=NaturezaJuridica.objects.all(), empty_label='', required=False, initial=0,
       widget=forms.Select(
           attrs={
               'id': 'natureza_juridica', 'class': 'selectpicker form-control', 'title': "", 'ng-model': 'natureza_juridica',
               'autocomplete': "off", 'data-live-search': "true",  # 'disabled':'',
           }
       )
    )

    main_activity = forms.ModelChoiceField(label='Código de Atividade Principal', queryset=EconomicActivity.objects.all(), empty_label='', required=False, initial=0,
       widget=forms.Select(
           attrs={
               'id': 'main_activity', 'class': 'selectpicker form-control', 'title': "", 'ng-model': 'main_activity',
               'autocomplete': "off", 'data-live-search': "true"
           }
       )
   )

    """
    registration_status = forms.ChoiceField(choices=options_status_register,required=False,initial=0,
        error_messages=ERRORS_MESSAGES,
        widget= forms.Select(
            attrs={
                'id': 'registration_status','name': 'registration_status', 'class': "form-control ",
                'type': "text",'ng-model': 'registration_status','hidden':'true'
            }
        )
    )
    """

    comments = forms.CharField(
        label="Observações",max_length= 500,required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'comments', 'name': 'comments', 'class': "form-control uppercase", 'cols':2,'rows':3,
                'type': "text", 'ng-model': 'comments'
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

    """ I N F O R M A C O E S   C O M P L E M E N T A R E S """
    entity_father = forms.CharField(label="Nome Completo do Pai", max_length=64, required=False,error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
        attrs={
            'id': 'entity_father', 'name': 'entity_father', 'class': "form-control uppercase", 'type': "text",
            'autocomplete': "off", 'ng-model': 'entity_father',
            }
        )
    )

    entity_mother = forms.CharField(label="Nome Completo da Mãe", max_length=64, required=False,error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
            'id': 'entity_mother', 'name': 'entity_mother', 'class': "form-control uppercase", 'type': "text",
            'autocomplete': "off", 'ng-model': 'entity_mother',
            }
        )
    )

    entity_conjuge = forms.CharField(label="Nome Completo do Conjuge", max_length=64, required=False,error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'entity_conjuge', 'name': 'entity_conjuge', 'class': "form-control uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_conjuge',
            }
        )
    )

    entity_occupation = forms.CharField(label="Profissão", max_length=64, required=False,error_messages=ERRORS_MESSAGES,
        widget=forms.TextInput(
            attrs={
                'id': 'entity_occupation', 'name': 'entity_occupation', 'class': "form-control uppercase", 'type': "text",
                'autocomplete': "off", 'ng-model': 'entity_occupation',
            }
        )
    )

    options_tributary_regime = (
        (0,""),
        (1, "MICRO EMPREENDEDOR INDIVIDUAL"),
        (2, "SIMPLES NACIONAL"), (3, "LUCRO PRESUMIDO"),
        (4, "LUCRO REAL")
    )

    options_relation_type = (
        ('0', ""),('1', "CLIENTE"), ('2', "FORNECEDOR"),
        ('3', "FUNCIONÁRIO"), ('4', "TRANSPORTADOR"),
        ('5', "REPRESENTANTE"),('6', "BANCO")
    )

    options_activity = (
        (1, "CONSUMIDOR"), (2, "COMÉRCIO"), (3, "SERVIÇOS"),
        (4, "INDÚSTRIA"), (5, "TRANSPORTE"), (6, "IMPORTAÇÃO"),
        (7, "EXPORTAÇÃO"), (8, "PRODUTOR RURAL"), (9, "EXTRATIVISTA"),
    )

    options_buy_destination = (
        (0, "CONSUMO"), (1, "REVENDA"), (2, "INSUMO DE PRODUÇÃO"),
        (3, "PRODUÇÃO"), (4, "PRESTAÇÃO DE SERVIÇO"),
    )

    tributary_regime = forms.ChoiceField(label='Regime Tributário', choices=options_tributary_regime, required=False, initial=0,
        widget=forms.Select(
         attrs={'id': 'tributary_regime', 'class': 'selectpicker form-control', 'title':"",'autocomplete': "off"}
        )
    )

    relations_company = forms.ChoiceField(label="Tipo de Relação", choices=options_relation_type, required=False, error_messages=ERRORS_MESSAGES,
        widget=forms.Select(
            attrs={'id': 'relations_company', 'class': 'selectpicker form-control multiple', 'multiple':'multiple','title':"", 'name': 'relations_company'}
        )
    )

    """
    delivery_route = forms.ModelChoiceField(
        label="Rota de Entrega", queryset=Contact.objects.all(), required=False, empty_label='Nenhum rota cadastrada',
        error_messages=ERRORS_MESSAGES,
        widget=forms.Select(
            attrs={
                'id': 'delivery_route', 'class': "selectpicker form-control optional",
                'autocomplete': "off", 'ng-model': 'delivery_route'
            }
        )
    )
    """

    buy_destination = forms.ChoiceField(label="Destino da Compra", choices=options_buy_destination, required=False,error_messages=ERRORS_MESSAGES,
         widget=forms.Select(
             attrs={'id': 'buy_destination', 'class': 'selectpicker form-control', 'multiple':"multiple", 'title':"", 'ng-model': 'buy_destination'}
         )
     )

    company_activities = forms.MultipleChoiceField(label="Tipo de Atividade",required=False, choices=options_activity,
        error_messages=ERRORS_MESSAGES, widget=forms.Select(
        attrs={'id': 'company_activities', 'class': 'selectpicker form-control multiple', 'multiple':'multiple', 'title':"", 'ng-model': 'company_activities'}))

    market_segments = forms.ModelMultipleChoiceField(label="Segmento de Mercado",required=False,queryset=MarketSegment.objects.all(),
        widget=forms.Select(
        attrs={'id': 'market_segments', 'class': 'selectpicker form-control','data-live-search':"true", 'multiple':"multiple",'title':'',  'ng-model': 'market_segments',
            'list': 'options_segments'}
        )
    )

    comments_fiscal_note = forms.CharField(
        label="Observações complementares da nota fiscal", max_length=128, required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'comments_fiscal_note', 'name': 'comments_fiscal_note', 'class': "form-control uppercase", 'cols': 2, 'rows': 4,
                'type': "text", 'ng-model': 'comments_fiscal_note','value':'ENTREGAR PREFERENCIALMENTE DAS 09H AS 16H.'
            }
        )
    )

"""
class EntityIdentificationFormOld(BaseForm):

    #def __init__(self, *args, **kwargs):
    #    super(AbstractFormEntity, self).__init__(*args, **kwargs)


    def clean(self):
        form_data = self.cleaned_data
        ""
        if len(self.cleaned_data) == len(self.fields):
            if form_data['password'] != form_data['confirm_password']:
                self._errors["password"] = [
                    "Confirme a Senha: Precisa ser igual ao campo Senha"]  # Will raise a error message
                del form_data['password']

            elif form_data['old_password'] == form_data['password']:
                self._errors["password"] = [
                    "Nova Senha: Precisa ser diferente da senha antiga."]  # Will raise a error message
                del form_data['password']
        ""
        return form_data

"""
"""
class EntityCompanyIdentificationForm(AbstractFormEntity):
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

    ""
    #def __init__(self, *args, **kwargs):
        super(AbstractFormEntity, self).__init__(*args, **kwargs)

        self.fields['cpf_cnpj'].widget.attrs['placeholder']             = 'CPF/CNPJ..'
        self.fields['entity_name'].widget.attrs['placeholder']          = 'Nome ou Razao..'
        self.fields['fantasy_name'].widget.attrs['placeholder']         = 'Nome Fantasia..'
        self.fields['birth_date_foundation'].widget.attrs['plaseholder']= "Data Nascimento/Fundação.."
        self.fields['market_segment'].widget.attrs['placeholder']       = "Segmento Mercado"
        self.fields['comments'].widget.attrs['placeholder']             = 'Obervações'
        self.fields['registration_status'].widget                       = forms.HiddenInput()
    ""
"""


class EntityPhoneForm (forms.Form, BaseForm):

    model = Contact

    options_phone_type = (
        (1, "CELULAR"),
        (2, "FIXO"),
        (3, "SAC"),
        (4, "FAX")
    )

    type_contact = forms.ChoiceField(
        label="Tipo",
        choices=options_phone_type,
        error_messages=ERRORS_MESSAGES,
        required=True,
        initial='CELL',
        widget=forms.Select(
            attrs={
                'id': 'type_contact', 'name': 'type_contact', 'class': "form-control",
                'type': "text", 'ng-model': 'type_contact'
            }
        )
    )

    name = forms.CharField(
        label="Nome",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'id': 'name_contact', 'name': 'name_contact', 'class': 'form-control uppercase', 'required':'true'
            }
        )
    )

    ddd = forms.CharField(
        label="Prefixo",
        required= True,
        max_length=4,
        widget= forms.TextInput(
            attrs={
                'id':'ddd','name':'ddd','class':'form-control', 'required':'true'
            }
        )
    )

    phone = forms.CharField(
        label="Telefone",
        required=True,
        max_length=10,
        widget= forms.TextInput(
            attrs={
                'id':'phone_number','name':'phone_number','class':'form-control', 'required':'true'
            }
        )
    )

    complemento = forms.CharField(
        label="Complemento",
        max_length=32,
        required=False,
        widget= forms.TextInput(
            attrs={
                'id':'complemento', 'name':'complemento ', 'class':'form-control uppercase'
            }
        )
    )

    '''comments = forms.CharField(
        label="Observações",
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={
                'id': 'observations', 'name': 'observations', 'class': "form-control", 'cols': 2, 'rows': 3,
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
    )'''

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


class EntityEmailForm (FormAbstractEmail,forms.Form, BaseForm):

    model = Email

    boolean_email = (
        (True,'Sim'),
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
                'id': 'name', 'name': 'name', 'class': 'form-control uppercase', 'ng-model': 'name', 'placeholder':'Nome..'
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
