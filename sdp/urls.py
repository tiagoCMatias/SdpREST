from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from sdp.views.Auth import AuthViewSet
from sdp.views.tipoTendas import TipoTendasViewSet
from sdp.views.configTenda import ConfigTendaViewSet
from sdp.views.CRM.cliente import ClienteViewModel
from sdp.views.CRM.obras import ObrasViewModel
from sdp.views.user import UserViewSet
from sdp.views.componentes.familiaComponentes import FamiliaComponentesViewModel
from sdp.views.componentes.componentes import ComponentesViewModel

router = routers.DefaultRouter()

router.register(r'tendas/tipos', TipoTendasViewSet, 'crud-tipo-tendas')
router.register(r'tendas/config', ConfigTendaViewSet, 'crud-config-tendas')

router.register(r'crm/clientes', ClienteViewModel, 'add-cliente')
router.register(r'crm/obra', ObrasViewModel, 'add-obra')
router.register(r'user', UserViewSet, 'crud-user')
router.register(r'componentes/familia', FamiliaComponentesViewModel, 'crud-family')

router.register(r'componentes/lista', ComponentesViewModel, 'crud-comp')


urlpatterns = [
    url(r'login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('', include(router.urls)),
]
