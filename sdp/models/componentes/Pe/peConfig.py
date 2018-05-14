from django.db import models

from sdp.models.configTenda import ConfigTenda
from sdp.models.componentes.Pe.pe import Pe


class peConfigQuerySet(models.QuerySet):
    pass


class peConfig(models.Model):
    id = models.AutoField(primary_key=True)
    pe = models.OneToOneField(Pe, on_delete=models.CASCADE, db_column='pe_id', primary_key=True)
    tipoConfig = models.ForeignKey(ConfigTenda, on_delete=models.CASCADE, db_column='configTenda_id')

    objects = peConfigQuerySet.as_manager()

    class Meta:
        db_table = 'peConfig'
        ordering = ['-id']
