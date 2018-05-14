from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from sdp.views.tipoTendas import TipoTendasViewSet
from sdp.views.configTenda import ConfigTendaViewSet
from sdp.views.componentes.viga import VigaViewModel

router = routers.DefaultRouter()

router.register(r'tendas/tipos', TipoTendasViewSet, 'crud-tipo-tendas')
router.register(r'tendas/config', ConfigTendaViewSet, 'crud-config-tendas')
router.register(r'componentes/adicionar', VigaViewModel, 'add-component')


urlpatterns = [
    path('', include(router.urls)),
]
