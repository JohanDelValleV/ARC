from rest_framework import routers, serializers, viewsets

from Rfid.models import Rfid

class RfidSerializers(serializers.ModelSerializer):
    nombre = serializers.ReadOnlyField(source='id_alumno.name')
    apellido = serializers.ReadOnlyField(source='id_alumno.lastname')
    _matricula = serializers.ReadOnlyField(source='id_alumno.matricula')
    class Meta:
        model = Rfid
        fields = ('__all__')