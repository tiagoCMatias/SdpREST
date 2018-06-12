from django.db import models


class userLevelQuerySet(models.QuerySet):
    def which_level(self, role_id):
        return self.filter(pk=role_id)

    def admin_level(self):
        return self.filter(title='Admin')

    def normal_level(self):
        return self.filter(title='Normal')

    def viewer_level(self):
        return self.filter(title='Viewer')


class UserLevel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, blank=False, null=True)
    description = models.CharField(max_length=512, blank=False, null=True)

    objects = userLevelQuerySet.as_manager()

    class Meta:
        db_table = 'UserLevels'
        ordering = ['-id']

    def __str__(self):
        return self.title