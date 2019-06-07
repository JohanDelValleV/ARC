from django.db import models

class Alumno(models.Model):
    name = models.CharField(max_length=254, null=False)
    

    def _str_(self):
        return self.name