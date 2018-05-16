from django.db import models

class ComponenteQuerySet(models.QuerySet):
    pass

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, blank=False, null=True)
    tag = models.CharField(max_length=32, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)

    objects = ComponenteQuerySet.as_manager()

    class Meta:
        db_table = 'componentesEstrutura'
        ordering = ['-id']

    def __str__(self):
        return self.nome

