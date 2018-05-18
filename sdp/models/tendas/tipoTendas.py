from django.db import models


class TipoTendaQuerySet(models.QuerySet):
    pass

class TipoTenda(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=False, null=True)
    description = models.CharField(max_length=512, blank=False, null=True)

    objects = TipoTendaQuerySet.as_manager()

    class Meta:
        db_table = 'tipoTenda'
        ordering = ['-id']

    def __str__(self):
        return self.title

