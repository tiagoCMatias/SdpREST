from django.db import models
from sdp.models.estrutura.componentes.componente import Componente

class VigaQuerySet(models.QuerySet):
    pass


class Viga(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, blank=False, null=True)
    tag = models.CharField(max_length=32, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, db_column='componente_id')
    quantidade = models.IntegerField(blank=False, null=False, default=0)

    objects = VigaQuerySet.as_manager()

    class Meta:
        db_table = 'viga'
        ordering = ['-id']

    def __str__(self):
        return self.nome

