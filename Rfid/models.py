from django.db import models
from django.utils import timezone

from Alumno.models import Alumno

class Rfid(models.Model):
    id_rfid = models.IntegerField(null=False)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    delete = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    def _str_(self):
        return self

    class Meta:
        db_table = 'Rfid'