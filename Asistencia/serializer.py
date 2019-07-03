from rest_framework import routers, serializers, viewsets

from Asistencia.models import Asistencia

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('__all__')
        