from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Rfid.models import Rfid
from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

# Create your views here.
 

class AsistenciaCheckout(APIView):
    def get(self, request, format=None):
        queryset = Asistencia.objects()
        serializer = AsistenciaSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        serializer = AsistenciaSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


