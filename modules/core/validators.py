import re


def is_empty(value):
    if len(value) == 0:
        return True
    else:
        return False


def contain_minimal_size(value,size):
    return check_pattern(r'\w{'+str(size)+',}', value)


def contain_numbers(value):
    return check_pattern(r'\d', value)


def contain_alpha(value):
    return check_pattern(r'[a-zA-Z]', value)


def check_pattern(pattern,value):
    if re.search(pattern, value):
        return True
    else:
        return False
