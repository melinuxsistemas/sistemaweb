import re
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def required_validator(value):
    if value is not None and value != "":
        return True
    else:
        raise ValidationError(_("This field is required."), code='required')
        return False


def minimum_age_person_validator(value):
    if value is None or value == '':
        return True
    value = format_date_value(value)
    print("OLHA O VALUE QUANDO VOLTA:",value)
    #Como não é um campo obrigatorio o validador nao pode retornar erro em alor None
    if value is not None:
        current_date = datetime.datetime.now().date()
        time_diff = ((current_date-value).days)/365.25
        if(time_diff < 18):
            raise ValidationError(_("birth_date_foundation: Age must be greather then 18 years"), code='minimum_age_person')
            return False
    else:
        raise ValidationError(_("birth_date_foundation: Date not is valid."), code='invalid')
    return True


def maximum_age_person_validator(value):
    value = format_date_value(value)
    if value is not None:
        current_date = datetime.datetime.now().date()
        time_diff = ((current_date - value).days) / 365.25
        if (time_diff > 150):
            print("O CARA EH MTO VELHO ",time_diff)
            raise ValidationError(_("birth_date_foundation: Person must be less then 150 years."), code='maximum_age_person')
            return False
    else:
        raise ValidationError(_("birth_date_foundation: Date not is valid."), code='invalid')
    return True


def future_birthdate_validator(value):
    value = format_date_value(value)
    if value is not None:
        current_date = datetime.datetime.now().date()
        if value > current_date:
            print("O CARA NASCEU NO FUTURO??!")
            raise ValidationError(_("birth_date_foundation: Date can not be future"), code='future_date')
            return False
    return True


def min_words_name_validator(value):
    if value is None or value == "":
        raise ValidationError(_("Name must contain at least two words"), code='name_min_words')
        return False

    result = re.search(r"\S \S", value)
    if result is None:
        raise ValidationError(_("Name must contain at least two words"), code='name_min_words')
        return False
    else:
        return True


def cpf_cnpj_validator(value):
    if len(value) == 11:
        return cpf_validator(value)
        #if not cpf_validator(value):
        #    raise ValidationError(_("cpf_cnpj: Cpf number is not valid."), code='document_invalid')
        #    return False
    elif len(value) == 14:
        return cnpj_validator(value)
        #if not cnpj_validator(value):
        #    raise ValidationError(_("cpf_cnpj: Cnpj number is not valid."), code='document_invalid')
        #    return False
    else:
        raise ValidationError(_("cpf_cnpj: Cpf ou Cnpj number is not valid."), code='document_invalid')
        return False
    return True


def format_date_value(value):
    if isinstance(value, datetime.date):
        return value
    elif isinstance(value, str):
        try:
            new_value = datetime.datetime.strptime(value, "%d/%m/%Y").date()
            return new_value
        except:
            #raise ValidationError(_("birth_date_foundation: Date not is valid."), code='invalid')
            return None
    else:
        return None


def cpf_validator(value):
    """
    Valida CPFs, retornando apenas a string de números válida.

    # CPFs errados
    >>> cpf_validator('abcdefghijk')
    False
    >>> cpf_validator('123')
    False
    >>> cpf_validator('')
    False
    >>> cpf_validator(None)
    False
    >>> cpf_validator('12345678900')
    False

    # CPFs corretos
    >>> cpf_validator('95524361503')
    True
    >>> cpf_validator('955.243.615-03')
    True
    >>> cpf_validator('  955 243 615 03  ')
    True
    """

    cpf = ''.join(re.findall('\d', str(value)))
    if (not cpf) or (cpf is None) or  (len(cpf) != 11):
        raise ValidationError(_("cpf_cnpj: Cpf number is not valid."), code='document_invalid')
        return False

    # Pega apenas os 9 primeiros dígitos do CPF e gera os 2 dígitos que faltam
    original_number = list(map(int, cpf))
    calculated_number = original_number[:9]

    while len(calculated_number) < 11:
        r = sum([(len(calculated_number) + 1 - i) * v for i, v in enumerate(calculated_number)]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        calculated_number.append(f)

    # Se o número gerado coincidir com o número original, é válido
    if calculated_number == original_number:
        return True

    raise ValidationError(_("cpf_cnpj: Cpf number is not valid."), code='document_invalid')
    return False


def cnpj_validator(value):
    """
    Valida CNPJs, retornando apenas a string de números válida.

    # CNPJs errados
    >>> cnpj_validator('abcdefghijklmn')
    False
    >>> cnpj_validator('123')
    False
    >>> cnpj_validator('')
    False
    >>> cnpj_validator(None)
    False
    >>> cnpj_validator('12345678901234')
    False
    >>> cnpj_validator('11222333000100')
    False

    # CNPJs corretos
    >>> cnpj_validator('11222333000181')
    True
    >>> cnpj_validator('11.222.333/0001-81')
    True
    >>> cnpj_validator('  11 222 333 0001 81  ')
    True
    """
    cnpj = ''.join(re.findall('\d', str(value)))

    if (not cnpj) or (cnpj is None) or (len(cnpj) != 14):
        raise ValidationError(_("cpf_cnpj: Cpf number is not valid."), code='document_invalid')
        return False

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    original_number = list(map(int, cnpj))
    calculated_number = original_number[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(calculated_number) < 14:
        r = sum([x * y for (x, y) in zip(calculated_number, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        calculated_number.append(f)
        prod.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if calculated_number == original_number:
        return True
    raise ValidationError(_("cpf_cnpj: Cpf number is not valid."), code='document_invalid')
    return False

def correct_length (value,size_menu):
    value = permission_to_list(value)
    if (len(value) == size_menu):
        return True
    raise ValidationError(_("Field size error: Please enter value with equal length."),code='length_wrong')

def validator_level (value):
    list = permission_to_list(value)
    for i in list:
        if ((i > 5) or (i < 0)):
            raise ValidationError(_("Field error: Please enter with correct value"), code='level_wrong')
    return True

def permission_to_list (string):
    string = string.split(';')
    list = []
    for i in string:
        try:
            list.append(int(i))
        except:
            raise ValidationError(_("Field error: Plese enter onlu number"),code='not_all_numeric')
    return list

def only_numeric(value):

    if value is not None:
        print('OLHA O VALUE:',value)
        if value.isnumeric():
            return True
    raise ValidationError(_("phone: Please enter value with only numeric type."), code='not_all_numeric')
    return False

def validate_ddd(value,type):
    size = len(value)
    if (type is not None):
        if ((int(type) == 3) and (size == 4)):
            return True
        if (size == 2):
            return True
        raise ValidationError(_("ddd: Prefix number is not valid"), code='not_all_numeric')
    return False

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()  # verbose=True)
    if result[0] == 0:
        print("OK!")
    else:
        print(result)