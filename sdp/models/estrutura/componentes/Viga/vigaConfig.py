from django.db import models

from sdp.models.configTenda import ConfigTenda
from sdp.models.estrutura.componentes.Viga.viga import Viga


class vigaConfigQuerySet(models.QuerySet):
    pass


class vigaConfig(models.Model):
    id = models.AutoField(primary_key=True)
    viga = models.ForeignKey(Viga, on_delete=models.CASCADE, db_column='viga_id')
    tipoConfig = models.ForeignKey(ConfigTenda, on_delete=models.CASCADE, db_column='configTenda_id')

    objects = vigaConfigQuerySet.as_manager()

    class Meta:
        db_table = 'vigaConfig'
        ordering = ['-id']


