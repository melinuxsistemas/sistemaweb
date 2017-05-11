from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from modules.core.config import MENSAGENS_ERROS
#from django.contrib.auth.hashers import check_password,make_password,is_password_usable

opcoes_tipos_usuarios = (
        ('A', 'ADMIN'),
        ('D', 'DESENVOLVEDOR'),
        ('S', 'SUPORTE'),
		('C', 'CONTRATANTE'),
		('F', 'FUNCIONARIO'),
	)

class GerenciadorUsuario(BaseUserManager):

    def _create_user(self,email,senha,super_user,conta_ativada,ativo,tipo):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email, account_activated=conta_ativada, active_user=ativo,type_user=tipo,is_superuser=super_user, last_update=now, joined_date=now)#, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def criar_usuario_contratante(self, email,senha):
        return self._create_user(email, senha,False,False, False,"C")

    def criar_usuario_funcionario(self, email,senha):
        return self._create_user(email, senha,False,False,False,"F")

    def criar_usuario_suporte(self, email, senha):
        return self._create_user(email, senha,False,False,False, "S")

    def criar_usuario_desenvolvedor(self, email, senha):
        return self._create_user(email, senha,False, False, False, "D")

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

    def authenticate(self, email=None, password=None):
        try:
            user = Usuario.objects.get_user_email(email)
            print("usuario",user)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            return None

    def get_user_email(self,email):
        try:
            result = Usuario.objects.get(email=email)
            print("Resultado ",result)
            return result
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None


class Usuario(PermissionsMixin, AbstractBaseUser):
    email             = models.EmailField(_('Email'), max_length=255, unique=True)
    type_user         = models.CharField("Tipo de Usuário:",max_length=1,null=False,default='F',error_messages=MENSAGENS_ERROS)
    joined_date       = models.DateTimeField(null=True, auto_now_add=True)
    last_update       = models.DateTimeField(null=True, auto_now=True)
    account_activated = models.BooleanField(default=False)
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

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    """def set_password(self, raw_password):
        senha = make_password(raw_password)
        print ("Veja a senha:", senha," - TAMANHO:",len(senha))
        return senha
    """