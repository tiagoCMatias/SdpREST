from django.db import models
from sdp.models.tendas.tipoTendas import TipoTenda

class ConfigTendaQuerySet(models.QuerySet):
    pass


class ConfigTenda(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=64, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)
    tipo = models.ForeignKey(TipoTenda, on_delete=models.CASCADE, db_column='tipoTenda_id')

    objects = ConfigTendaQuerySet.as_manager()

    class Meta:
        db_table = 'configTenda'
        ordering = ['-id']

    def __str__(self):
        return self.title

