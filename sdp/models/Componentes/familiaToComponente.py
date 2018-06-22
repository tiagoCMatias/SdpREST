from django.db import models

#Models
from sdp.models.Componentes.componente import Componente
from sdp.models.Tendas.configTenda import ConfigTenda


class FamiliaToComponentesQuerySet(models.QuerySet):
    pass


class FamiliaToComponentes(models.Model):
    id = models.AutoField(primary_key=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, db_column='componente_id', related_name='pertence')
    tenda = models.ForeignKey(ConfigTenda, on_delete=models.CASCADE, db_column='tenda_id')

    objects = FamiliaToComponentesQuerySet.as_manager()

    class Meta:
        db_table = 'FamiliaToComponentes'
        ordering = ['-id']

    def __str__(self):
        return self.componente

