from django.test import TestCase
from modules.user.models import *
from modules.core.validators import *
#from django.utils import timezone
#from django.core.urlresolvers import reverse
#from whatever.forms import WhateverForm


class ValidatorsTest(TestCase):

    def test_emtpy_validator(self):
        self.assertEqual(is_empty(""), True, "Testar Validacao de valor vazio para campo vazio (OK)")
        self.assertEqual(is_empty("teste"), False, "Testar Validacao de valor vazio para campo preenchido (OK)")




