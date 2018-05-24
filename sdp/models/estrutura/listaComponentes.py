from django.db import models

#Models
from sdp.models.estrutura.componentes.componente import Componente
from sdp.models.tendas.configTenda import ConfigTenda


class ListaDeComponentesQuerySet(models.QuerySet):
    pass


class ListaDeComponentes(models.Model):
    id = models.AutoField(primary_key=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, db_column='componente_id', related_name='pertence')
    tenda = models.ForeignKey(ConfigTenda, on_delete=models.CASCADE, db_column='tenda_id')

    objects = ListaDeComponentesQuerySet.as_manager()

    class Meta:
        db_table = 'ListaDeComponentes'
        ordering = ['-id']

    def __str__(self):
        return self.componente

