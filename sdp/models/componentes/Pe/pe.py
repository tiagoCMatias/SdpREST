from django.db import models

class PeQuerySet(models.QuerySet):
    pass


class Pe(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, blank=False, null=True)
    tag = models.CharField(max_length=32, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)

    objects = PeQuerySet.as_manager()

    class Meta:
        db_table = 'pe'
        ordering = ['-id']

    def __str__(self):
        return self.title

