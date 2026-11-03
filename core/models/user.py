
from datetime import date

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from uploader.models import Image


CARGO_CHOICES = (
    ('chefe', 'Chefe'),
    ('gerente', 'Gerente'),
    ('nutricionista', 'Nutricionista'),
    ('cuidador', 'Cuidador'),
)


class AdministradorManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email or not email.strip():
            raise ValueError('O usuário precisa ter um endereço de email.')

        email = self.normalize_email(email).strip()

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário precisa ter is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário precisa ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Administrador(AbstractBaseUser, PermissionsMixin):

    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('foto'),
        help_text=_('Foto de perfil do administrador'),
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_('email'),
        help_text=_('Email'),
    )

    nome = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('nome'),
        help_text=_('Nome completo'),
    )

    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name=_('telefone'),
        help_text=_('Telefone'),
    )

    cargo = models.CharField(
        max_length=50,
        choices=CARGO_CHOICES,
        blank=True,
        null=True,
        verbose_name=_('cargo'),
        help_text=_('Cargo do administrador'),
    )

    data_registro = models.DateField(
        default=date.today,
        verbose_name=_('data de registro'),
        help_text=_('Data de registro'),
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Usuário está ativo'),
        help_text=_('Indica que este usuário está ativo.'),
    )

    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Usuário é da equipe'),
        help_text=_('Indica que este usuário pode acessar o Admin.'),
    )

    objects = AdministradorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return self.nome or self.email
