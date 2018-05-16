from django.urls import path, include
from rest_framework import routers

from sdp.views.tipoTendas import TipoTendasViewSet
from sdp.views.configTenda import ConfigTendaViewSet
from sdp.views.componentes.viga import VigaViewModel
from sdp.views.CRM.cliente import ClienteViewModel
from sdp.views.CRM.obras import ObrasViewModel
from sdp.views.user import UserViewSet

router = routers.DefaultRouter()

router.register(r'tendas/tipos', TipoTendasViewSet, 'crud-tipo-tendas')
router.register(r'tendas/config', ConfigTendaViewSet, 'crud-config-tendas')
router.register(r'componentes/adicionar/viga', VigaViewModel, 'add-viga')

router.register(r'crm/clientes', ClienteViewModel, 'add-cliente')
router.register(r'crm/obra', ObrasViewModel, 'add-obra')
router.register(r'user', UserViewSet, 'crud-user')


urlpatterns = [
    path('', include(router.urls)),
]
