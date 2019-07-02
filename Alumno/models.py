from django.db import models
from django.utils import timezone


class Alumno(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    matricula = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Alumno'