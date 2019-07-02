from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Asistencia.models import Asistencia
from Asistencia.serializer import AsistenciaSerializers

# Create your views here.






