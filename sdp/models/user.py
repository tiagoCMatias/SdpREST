from datetime import datetime
from django.db import models
from sdp.models.userLevel import UserLevel


class UserQuerySet(models.QuerySet):
    def match_credentials(self, username, password):
        return self.filter(username=username, password=password)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64, blank=False, null=True, unique=True)
    username = models.CharField(max_length=64, blank=False, null=True)
    password = models.CharField(max_length=64, blank=False, null=True)
    level = models.ForeignKey(UserLevel, on_delete=models.CASCADE, db_column='level_id', related_name='level')
    #added = models.DateTimeField(auto_now_add=True, blank=True)
    #updated = models.DateTimeField(auto_now=True, blank=True)

    objects = UserQuerySet.as_manager()

    class Meta:
        db_table = 'users'
        ordering = ['-id']

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.level.title == 'Admin'

    @property
    def is_normal(self):
        return self.level.title == 'Normal'

    @property
    def is_viewer(self):
        return self.level.title == 'View'
