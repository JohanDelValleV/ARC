from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Rfid.views import RfidDetail, RfidList
from Rfid.serializer import RfidSerializers

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
        x = datetime.now()
        data = RfidDetail.get_object(self, request.POST['rfidn'])
        print(data)
        if(data == 404):                                                                
            RfidList.post(self, request, format=None)       
            print('i') 
        serializer = AsistenciaSerializers(data = request.data)
        
        if serializer.is_valid():
            id_rfid = int(request.POST['rfid'])                   
            # print ("Formato dd/mm/yyyy =  %s-%s-%s" % (x.year, x.month, x.day) )
            # fecha1 =" %s-0%s-0%s" % (x.year, x.month, x.day) 
            # from datetime import datetime
            a = str(x.year)
            m = str(x.month)
            d = str(x.day)
            fechaCompara = a + "-" + m + "-" + d
            print(a + "-" + m + "-" + d)

                  
            try:
                post = Asistencia.objects.filter(rfid_id=id_rfid,fecha= datetime.strptime(fechaCompara, "%Y-%m-%d").date())
                print(post)     
                print("hola")
                if post[1].rfid_id == id_rfid and post[1].fecha == datetime.strptime(fechaCompara, "%Y-%m-%d").date():
                    return Response('Ya existe')
                # else:
                #     serializer.save()
                #     datas = serializer.data
                #     return Response(datas)        
            except:
                serializer.save()
                datas = serializer.data
                return Response(datas)    

                
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)