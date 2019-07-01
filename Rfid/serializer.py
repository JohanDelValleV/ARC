from rest_framework import routers, serializers, viewsets

from Rfid.models import Rfid
from Alumno.models import Alumno

class RfidSerializers(serializers.ModelSerializer):
    id_alumno = serializers.CharField(source='id_rfid')
    class Meta:
        model = Rfid
        fields = ('__all__')

# class AlumnoRfidSerailizers(serializers.ModelSerializer):
#     # nameRfid = serializers.ReadOnlyField(source='alumno.name')
#     # lastnameRfid = serializers.ReadOnlyField()
#     # matriculaRfid = serializers.ReadOnlyField()

#     class Meta:
#         model = Alumno
#         fields = '__all__'