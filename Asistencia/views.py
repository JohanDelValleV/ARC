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


from datetime import datetime, timedelta, date
import time
# Create your views here.

class AsistenciaCheckout(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            data = Rfid.objects.get(id_rfid=request.POST['rfid'])
        except:
            return Response(404)

        x = datetime.now()
      
        id_rfid = int(request.POST['rfid'])  
        a = str(x.year)
        m = str(x.month)
        d = str(x.day)
        fechaCompara = a + "-" + m + "-" + d
        print(a + "-" + m + "-" + d)
                
        try:
            post = Asistencia.objects.get(rfid_id=data.id,fecha= datetime.strptime(fechaCompara, "%Y-%m-%d").date())
            print(post)     
            if post.rfid_id == id_rfid and post.fecha == datetime.strptime(fechaCompara, "%Y-%m-%d").date():
                return Response('Ya existe')
            else:
                 return Response('Ya existe jaja')     
        except:
            datos= {"rfid":data.id,"rfidn":data.id_rfid,"id_alumno":data.id_alumno,"id_rfid":data.id_rfid}
            serializer = AsistenciaSerializers(data = datos)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.data)
        
                
        #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



       


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



