from modules.core.forms import FormAbstractEntity


class FormRegister (FormAbstractEntity):

    def __init__(self, *args, **kwargs):
        super(FormAbstractEntity, self).__init__(*args, **kwargs)
        self.fields['cpf_cnpj'].widget.attrs['placeholder'] = 'CPF/CNPJ..'
        self.fields['nome_razao'].widget.attrs['placeholder'] = 'Nome ou Razao..'
        self.fields['nome_fantasia'].widget.attrs['placeholder'] = 'Nome Fantasia..'