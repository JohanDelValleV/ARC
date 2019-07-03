from rest_framework import routers, serializers, viewsets

from Asistencia.models import Asistencia

class AsistenciaSerializers(serializers.ModelSerializer):
    _nombre = serializers.ReadOnlyField(source='rfid.id_alumno.name')
    _lastname = serializers.ReadOnlyField(source='rfid.id_alumno.lastname')
    class Meta:
        model = Asistencia
        fields = ('__all__')
        