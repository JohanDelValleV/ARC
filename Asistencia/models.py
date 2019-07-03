from django.db import models
from django.utils import timezone
from Rfid.models import Rfid

# Create your models here.
class Asistencia(models.Model):
    rfid= models.ForeignKey(Rfid,on_delete=models.CASCADE)
    create = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.name

    class Meta:
        db_table = 'Asistencia'