from datetime import datetime
from django.db import models
from sdp.models.CRM.cliente import Cliente

class ObrasQuerySet(models.QuerySet):
    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset

class Obras(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    local = models.CharField(max_length=64, blank=False, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_id')

    objects = ObrasQuerySet.as_manager()

    class Meta:
        db_table = 'obras'
        ordering = ['-id']

    #def __str__(self):
    #    return self.objects.filter().get()

