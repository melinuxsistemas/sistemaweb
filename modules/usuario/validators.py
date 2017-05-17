import re

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from modules.usuario.models import Usuario
from modules.core.validators import is_empty,contain_alpha,contain_numbers,contain_minimal_size

email_format_validator = EmailValidator(message="Erro! Email inválido.")

def email_unique_validator(value):
    if len(Usuario.objects.filter(email=value)) != 0:
        raise ValidationError(_('Error! %(value) not unique.'),
            params={'value': value},
        )

def password_format_validator(value):
    if (is_empty(value) or not contain_minimal_size(value,8) or not contain_alpha(value) or not contain_numbers(value)):
        raise ValidationError(_('Error! %(value) must be 8 characters or more with numbers and letters'),
            params={'value': value},
        )