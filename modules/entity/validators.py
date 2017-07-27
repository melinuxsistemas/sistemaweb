import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def cpf_cnpj_validator(value):
    if len(value) == 11:
        if not cpf_validator(value):
            raise ValidationError(_("Cpf number not is valid."), code='integrity')
            return False
    else:
        if not cnpj_validator(value):
            raise ValidationError(_("Cnpj number not is valid."), code='integrity')
            return False
    return True


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

    if (not cpf) or (len(cpf) < 11):
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

    if (not cnpj) or (len(cnpj) < 14):
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
    return False

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()  # verbose=True)
    if result[0] == 0:
        print("OK!")
    else:
        print(result)