import re

def cpf_is_valid(value):
    if value is not None and not is_empty(value) and contain_minimal_size(value, 8) and contain_numbers(value) and contain_alpha(value):
        return True
    else:
        return False