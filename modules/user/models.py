from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission
from modules.core.config import ERRORS_MESSAGES
from modules.core.utils import generate_activation_code
from modules.core.validators import check_password_format
from modules.entity.models import Contact
from modules.user.validators import email_format_validator,email_dangerous_symbols_validator


opcoes_tipos_usuarios = (
        ('A', 'ADMIN'),
        ('D', 'DESENVOLVEDOR'),
        ('S', 'SUPORTE'),
        ('C', 'CONTRATANTE'),
        ('F', 'FUNCIONARIO'),
)


class UserManager(BaseUserManager):

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
        result = User.objects.filter(activation_code=activation_code)
        if len(result) == 0:
            return True
        elif len(result) == 1 and result[0].type_user == 'T':
            return True
        else:
            return False

    def authenticate(self,request, email=None, password=None):
        try:
            user = User.objects.get_user_email(email)
            if user.check_password(password):
                return user
            return None

        except:
            return None

    def get_user_email(self,email):
        try:
            result = User.objects.get(email=email)
            return result
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class User(PermissionsMixin, AbstractBaseUser):
    email             = models.EmailField(_('Email'), max_length=255, unique=True, validators=[email_format_validator, email_dangerous_symbols_validator], error_messages=ERRORS_MESSAGES)
    type_user         = models.CharField("Tipo de Usuário:", max_length=1, null=False, default='F', error_messages=ERRORS_MESSAGES)
    joined_date       = models.DateTimeField(null=True, auto_now_add=True)
    last_update       = models.DateTimeField(null=True, auto_now=True)
    account_activated = models.BooleanField(default=False)
    activation_code   = models.CharField(max_length=46, null=True, blank=True, error_messages=ERRORS_MESSAGES)
    active_user       = models.BooleanField(default=False)

    USERNAME_FIELD    = 'email'
    REQUIRED_FIELDS   = []

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')


    def user_gains_perms(request, user_id):
        user = get_object_or_404(User, email=user_id)
        # any permission check will cache the current set of permissions
        user.has_perm('myapp.change_blogpost')

        content_type = ContentType.objects.get_for_model(Contact)
        permission = Permission.objects.get(
            codename='change_blogpost',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        # Checking the cached permission set
        user.has_perm('myapp.change_blogpost')  # False

        # Request new instance of User
        # Be aware that user.refresh_from_db() won't clear the cache.
        user = get_object_or_404(User, pk=user_id)

        # Permission cache is repopulated from the database
        user.has_perm('myapp.change_blogpost')  # True

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


class Session(models.Model):
    class Meta:
        db_table = 'user_session'
        verbose_name = _('Sessão')
        verbose_name_plural = _('Sessões')

    session_key = models.CharField("Chave de Sessão", max_length=32, null=False, error_messages=ERRORS_MESSAGES)

    user = models.ForeignKey('User')
    internal_ip = models.GenericIPAddressField("IP Interno:", null=False, error_messages=ERRORS_MESSAGES)
    external_ip = models.GenericIPAddressField("IP Externo:", null=False, error_messages=ERRORS_MESSAGES)
    country_name = models.CharField("País", max_length=50, null=False, error_messages=ERRORS_MESSAGES)
    country_code = models.CharField("Sigla do País", max_length=2, null=False, error_messages=ERRORS_MESSAGES)
    region_code  = models.CharField("Sigla do Estado", max_length=2, null=False, error_messages=ERRORS_MESSAGES)
    region_name  = models.CharField("Estado", max_length=60, null=False, error_messages=ERRORS_MESSAGES)
    city         = models.CharField("Cidade", max_length=100, null=False, error_messages=ERRORS_MESSAGES)
    zip_code     = models.CharField("Código Postal", max_length=10, null=False, error_messages=ERRORS_MESSAGES)
    time_zone    = models.CharField("Fuzo Horário", max_length=30, null=False, error_messages=ERRORS_MESSAGES)
    latitude     = models.CharField("Latitude", max_length=20, null=False, error_messages=ERRORS_MESSAGES)
    longitude    = models.CharField("Longitude", max_length=20, null=False, error_messages=ERRORS_MESSAGES)

    is_expired   = models.BooleanField("Sessão Expirada", null=False,blank=False, default=False,error_messages=ERRORS_MESSAGES)
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    terminate_date = models.DateTimeField(auto_now=True, null=False)


class SessionTask(models.Model):
    class Meta:
        db_table = 'user_session_task'
        verbose_name = _('Tarefa de Sessão')
        verbose_name_plural = _('Tarefas de Sessões')

    options_types_tasks = (
        (1, "REQUEST PAGE"),
        (2, "REQUEPES SERVICE"),
    )

    task_type    = models.CharField("Tipo da Requisição", max_length=1, null=False, default=2, choices=options_types_tasks, error_messages=ERRORS_MESSAGES)
    task_path    = models.CharField("Requisição", max_length=200, null=False, error_messages=ERRORS_MESSAGES)

    server_process_duration = models.PositiveIntegerField("Tempo de Processamento no Servidor (milisegundos)",null=True, blank=True)
    client_loading_duration = models.PositiveIntegerField("Tempo de Recebimento da Página (milisegundos)",null=True, blank=True)
    client_service_duration = models.PositiveIntegerField("Tempo de Carregamento dos Serviços (milisegundos)",null=True, blank=True)
    client_request_duration = models.PositiveIntegerField("Duração da Requisição (milisegundos)", null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, null=False)

    #SESSION_PARAMTERS['init_load_page'] = ''
    #SESSION_PARAMTERS['load_page_duration'] = ''
    #SESSION_PARAMTERS['setup_page_duration'] = ''
