from django.db import models
from django.utils import timezone

class Example(models.Model):
    name = models.CharField(max_length=254, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Example'
