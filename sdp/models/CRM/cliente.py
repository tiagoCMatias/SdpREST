from django.db import models

class ClientQuerySet(models.QuerySet):
    def match_cliente(self, nome):
        if self.filter(nome=nome):
            return self.filter(nome=nome).get()
        else:
            return ""

    def get_nome(self, id):
        if self.filter(pk=id):
            return self.filter(pk=id).get()


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64, blank=False, null=True, unique=True)
    descricao = models.CharField(max_length=512, blank=False, null=True)

    objects = ClientQuerySet.as_manager()

    class Meta:
        db_table = 'cliente'
        ordering = ['-id']



