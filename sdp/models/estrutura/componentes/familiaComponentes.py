from django.db import models

class FamiliaComponentesQuerySet(models.QuerySet):
    def familia_exist(self, id):
        if(self.filter(id=id)):
            return True
        else:
            return False

class FamiliaComponentes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=128, blank=False, null=True)
    tag = models.CharField(max_length=32, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)

    objects = FamiliaComponentesQuerySet.as_manager()

    class Meta:
        db_table = 'familiaComponente'
        ordering = ['-id']

    def __str__(self):
        return self.nome

