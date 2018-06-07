from django.db import models

#Models
from sdp.models.estrutura.componentes.familiaComponentes import FamiliaComponentes


class ComponenteQuerySet(models.QuerySet):
    def count_familia(self, familia):
        return self.filter(familia=familia).count()


class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, blank=False, null=True)
    peso = models.IntegerField(blank=False, null=True, default=0)
    descricao = models.CharField(max_length=512, blank=False, null=True)
    familia = models.ForeignKey(FamiliaComponentes, on_delete=models.CASCADE, db_column='familiaComponente_id')
    quantidade = models.IntegerField(blank=False, null=True, default=0)
    genCodigo = models.CharField(max_length=32, blank=False, null=True, unique=True)

    objects = ComponenteQuerySet.as_manager()

    class Meta:
        db_table = 'componentesEstrutura'
        ordering = ['-id']

    def __str__(self):
        return self.nome

