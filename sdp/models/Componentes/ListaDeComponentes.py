from django.db import models

#Models
from sdp.models.Componentes.componente import Componente


class ListaDeComponentesQuerySet(models.QuerySet):
    pass


class ListaDeComponentes(models.Model):
    id = models.AutoField(primary_key=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, db_column='componente_id')
    quantidade = models.IntegerField(blank=False, null=True, default=0)
    codigoLista = models.CharField(max_length=64, blank=False, null=True)

    objects = ListaDeComponentesQuerySet.as_manager()

    class Meta:
        db_table = 'ListaDeComponentes'
        ordering = ['-id']

    def __str__(self):
        return self.componente

