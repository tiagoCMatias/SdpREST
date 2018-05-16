from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UserQuerySet(models.QuerySet):
    def match_credentials(self, username, password):
        return self.filter(username=username, password=password)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=False, null=True)
    email = models.CharField(max_length=64, blank=False, null=True, unique=True)
    username = models.CharField(max_length=64, blank=False, null=False)
    password = models.CharField(max_length=64, blank=False, null=True)

    objects = UserQuerySet.as_manager()

    class Meta:
        db_table = 'users'
        ordering = ['-id']

    def __str__(self):
        return self.name
