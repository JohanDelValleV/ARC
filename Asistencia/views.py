from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Rfid.views import RfidDetail, RfidList

from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

# Create your views here.
class AsistenciaCheckout(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects()
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, rfid, format=None):
        data = RfidDetail.get_object(self, rfid)
        if(data != 404):
            RfidList.post(self, request, format=None)
        else:
            data = 1
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


