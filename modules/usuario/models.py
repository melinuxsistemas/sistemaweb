from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from modules.core.config import MENSAGENS_ERROS
from modules.core.utils import generate_activation_code
from modules.core.validators import check_password_format
from modules.usuario.validators import email_format_validator,email_dangerous_symbols_validator


opcoes_tipos_usuarios = (
        ('A', 'ADMIN'),
        ('D', 'DESENVOLVEDOR'),
        ('S', 'SUPORTE'),
        ('C', 'CONTRATANTE'),
        ('F', 'FUNCIONARIO'),
)


class GerenciadorUsuario(BaseUserManager):

    def _create_user(self, email, password, super_user, account_activated, active, tipo):
        if check_password_format(password):
            now = timezone.now()
            email = self.normalize_email(email)
            user = self.model(email=email, account_activated=account_activated, active_user=active,type_user=tipo,is_superuser=super_user, last_update=now, joined_date=now)#, **extra_fields)
            user.set_password(password)
            try:
                user.full_clean()
                user.save(using=self._db)
                return user

            except Exception as e:
                return e
        else:
            #raise ValueError('Passwords there are 8 or more characters, including letters and numbers.')
            return None

    def create_contracting_user(self, email, senha):
        return self._create_user(email, senha,False,False, False,"C")

    def create_functionary_user(self, email, senha):
        return self._create_user(email, senha,False,False,False,"F")

    def create_suport_user(self, email, senha):
        return self._create_user(email, senha,False,False,False, "S")

    def create_developer_user(self, email, senha):
        return self._create_user(email, senha,False, False, False, "D")

    def create_test_user(self, email, senha):
        user = self._create_user(email, senha, False, False, False, "T")
        if user is not None:
            activation_code = generate_activation_code(email)
            user.account_activated = True
            user.activation_code = activation_code
            try:
                user.save()
                return user
            except:
                return None
        return None

    def create_superuser(self, email, password):
        user = self._create_user(email, password, True,True, True, "A")
        user.is_active = True
        user.save(using=self._db)
        return user

    def check_available_email(self, email):
        if len(self.model.objects.filter(email=email)) == 0:
            return True
        else:
            return False

    def activation_code_is_unique(self, activation_code):
        result = Usuario.objects.filter(activation_code=activation_code)
        if len(result) == 0:
            return True
        elif len(result) == 1 and result[0].type_user == 'T':
            return True
        else:
            return False

    def authenticate(self,request, email=None, password=None):
        try:
            user = Usuario.objects.get_user_email(email)
            if user.check_password(password):
                return user
            return None

        except:
            return None

    def get_user_email(self,email):
        try:
            result = Usuario.objects.get(email=email)
            return result
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None


class Usuario(PermissionsMixin, AbstractBaseUser):
    email             = models.EmailField(_('Email'), max_length=255, unique=True,validators=[email_format_validator, email_dangerous_symbols_validator],error_messages=MENSAGENS_ERROS)
    type_user         = models.CharField("Tipo de Usuário:",max_length=1,null=False,default='F',error_messages=MENSAGENS_ERROS)
    joined_date       = models.DateTimeField(null=True, auto_now_add=True)
    last_update       = models.DateTimeField(null=True, auto_now=True)
    account_activated = models.BooleanField(default=False)
    activation_code   = models.CharField(max_length=46,null=True,blank=True,error_messages=MENSAGENS_ERROS)
    active_user       = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = GerenciadorUsuario()

    class Meta:
        db_table = 'usuario'
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __unicode__(self):
        return self.email

    def change_password(self,value):
        if check_password_format(value):
            self.set_password(value)
            self.save()
            return True
        else:
            return False

    def activate_account(self):
        self.account_activated(True)
        self.save()
        return True

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])