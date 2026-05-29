from django.contrib import admin
from django.urls import include, path
from click.utils import R
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from core.views import AdministradorRegistrationView, AdministradorViewSet, AlergiaRestricaoViewSet, AplicacaoMedicamentosViewSet, AtendimentoViewSet, AvaliacaoNutricionalViewSet, FichaMedicaViewSet, MedicamentosViewSet, MedicamentosPrescricaoViewSet, OcorrenciaViewSet, PedidosMedicamentoViewSet, PrescricaoViewSet, ResidenteViewSet, RotinaResidentesViewSet

router = DefaultRouter()
router.register(r'administradores', AdministradorViewSet, basename='administradores')
router.register(r'alergiarestricoes', AlergiaRestricaoViewSet, basename='alergiarestricoes')
router.register(r'aplicacoes', AplicacaoMedicamentosViewSet, basename='aplicacoes')
router.register(r'atendimentos', AtendimentoViewSet, basename='atendimentos')
router.register(r'avaliacaonutricionais', AvaliacaoNutricionalViewSet, basename='avaliacaonutricionais')
router.register(r'fichasmedicas', FichaMedicaViewSet, basename='fichasmedicas')
router.register(r'medicamentos', MedicamentosViewSet, basename='medicamentos')
router.register(r'medicamentosprescricoes', MedicamentosPrescricaoViewSet, basename='medicamentosprescricoes')
router.register(r'ocorrencias', OcorrenciaViewSet, basename='ocorrencias')
router.register(r'pedidosmedicamentos', PedidosMedicamentoViewSet, basename='pedidosmedicamentos')
router.register(r'prescricoes', PrescricaoViewSet, basename='prescricoes')
router.register(r'residentes', ResidenteViewSet, basename='residentes')
router.register(r'rotinaresidentes', RotinaResidentesViewSet, basename='rotinaresidentes')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de administradores
    path('api/registro/', AdministradorRegistrationView.as_view(), name='administrador_registration'),
    # API
    path('api/', include(router.urls)),
]
