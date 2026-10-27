from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
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

from core.views import (
    AdministradorRegistrationView,
    AdministradorViewSet,
    AlergiaRestricaoViewSet,
    AnotacaoCalendarioViewSet,
    AplicacaoMedicamentosViewSet,
    AtendimentoViewSet,
    AvaliacaoNutricionalViewSet,
    CuidadosPessoaisViewSet,
    DadosMedicosViewSet,
    FichaMedicaViewSet,
    MedicamentosPrescricaoViewSet,
    MedicamentosViewSet,
    OcorrenciaViewSet,
    PedidosMedicamentoViewSet,
    PrescricaoViewSet,
    ResidenteViewSet,
    RotinaResidentesViewSet,
)
from uploader.router import router as uploader_router

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
router.register(r'dadosmedicos', DadosMedicosViewSet, basename='dadosmedicos')
router.register(r'cuidadospessoais', CuidadosPessoaisViewSet, basename='cuidadospessoais')
router.register(r'anotacoes', AnotacaoCalendarioViewSet, basename='anotacoes')

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
    path('api/media/', include(uploader_router.urls)),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de administradores
    path('api/registro/', AdministradorRegistrationView.as_view(), name='administrador_registration'),
    # API
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)


from django.views.generic import RedirectView
from django.urls import path

urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
