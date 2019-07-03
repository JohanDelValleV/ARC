

from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Rfid.views import RfidDetail, RfidList
from Rfid.serializer import RfidSerializers

#Rfid
from Rfid.models import Rfid


from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

# Create your views here.
class AsistenciaCheckout(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            data = Rfid.objects.get(id_rfid=request.POST['rfidn'])
        except:
            return Response(404)
        datos= {"rfid":data.id,"rfidn":data.id_rfid,"id_alumno":data.id_alumno,"id_rfid":data.id_rfid}
        serializer = AsistenciaSerializers(data = datos)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response(serializer.data)
        


    # def post(self, request, format=None):
    #     data = RfidDetail.get_object(self, request.POST['rfidn'])
    #     print(data)
    #     if(data == 404):
    #         #
    #         print('hola')
    #         RfidList.post(self, request, format=None)
    #     print('data')
    #     serializer = AsistenciaSerializers(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         datas = serializer.data
    #         return Response(datas)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



