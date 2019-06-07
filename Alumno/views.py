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
        serializer = AlumnoSerializers(queryset)
        return Response(serializer.data)
