from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Alumno.models import Alumno
from Alumno.serializer import AlumnoSerializers

class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumnoDetail(APIView):
    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id)
        except Alumno.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno)
            return Response(serializer.data)
        else:
            return Response(alumno)

    def put(self, request, id, format=None):
        alumno = self.get_object(id)
        if alumno != 404:
            serializer = AlumnoSerializers(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
            else:
                return Response(alumno, status = status.HTTP_400_BAD_REQUEST)
            
