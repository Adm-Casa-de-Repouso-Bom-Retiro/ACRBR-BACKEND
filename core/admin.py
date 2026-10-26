"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class AdministradorAdmin(BaseUserAdmin):
    """Define the admin pages for administradores."""

    ordering = ['id']
    list_display = ['email', 'nome', 'cargo']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Info'),
            {
                'fields': (
                    'nome',
                    'telefone',
                    'cargo',
                    'data_registro',
                    'foto',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )

    readonly_fields = ['last_login']

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'nome',
                    'telefone',
                    'cargo',
                    'data_registro',
                    'foto',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


class ResidenteAdmin(admin.ModelAdmin):
    """Define the admin pages for residentes."""

    ordering = ['id']
    list_display = ['id', 'nome_completo', 'quarto', 'grau_dependencia', 'data_admissao']
    list_filter = ['grau_dependencia']
    search_fields = ['nome_completo', 'nome_responsavel', 'nome_responsavel_2']


class RotinaResidentesAdmin(admin.ModelAdmin):
    """Define the admin pages for rotinas de residentes."""

    ordering = ['id']
    list_display = ['id', 'residente', 'categoria', 'horario', 'dias_semana']
    list_filter = ['dias_semana', 'categoria']
    search_fields = ['categoria', 'descricao']


class DadosMedicosAdmin(admin.ModelAdmin):
    """Define the admin pages for dados médicos."""

    ordering = ['id']
    list_display = [
        'id',
        'residente',
        'peso',
        'altura',
        'peso_altura',
        'condicoes_medicas',
        'alergias',
        'sem_alergias_conhecidas',
    ]
    list_filter = ['sem_alergias_conhecidas']
    search_fields = ['condicoes_medicas', 'alergias', 'observacoes', 'residente__nome_completo']


class CuidadosPessoaisAdmin(admin.ModelAdmin):
    """Define the admin pages for cuidados pessoais."""

    ordering = ['id']
    list_display = ['id', 'residente', 'ajuda_banho', 'risco_queda', 'ajuda_alimentar']
    list_filter = ['ajuda_banho', 'risco_queda', 'ajuda_alimentar']
    search_fields = ['observacoes', 'residente__nome_completo']


class AnotacaoCalendarioAdmin(admin.ModelAdmin):
    """Define the admin pages for anotações do calendário."""

    ordering = ['id']
    list_display = [
        'id',
        'residente',
        'data',
        'hora',
        'categoria',
        'status',
        'titulo',
        'autor',
        'criado_em',
    ]
    list_filter = ['categoria', 'status', 'data']
    search_fields = ['titulo', 'texto', 'residente__nome_completo', 'autor__nome']


admin.site.register(models.Administrador, AdministradorAdmin)
admin.site.register(models.Residente, ResidenteAdmin)
admin.site.register(models.RotinaResidentes, RotinaResidentesAdmin)
admin.site.register(models.DadosMedicos, DadosMedicosAdmin)
admin.site.register(models.CuidadosPessoais, CuidadosPessoaisAdmin)
admin.site.register(models.AnotacaoCalendario, AnotacaoCalendarioAdmin)
