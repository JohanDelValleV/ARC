from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from example.models import Example
from example.serializer import ExampleSerializers

class ExampleList(APIView):
    def get(self, request, format=None):
        queryset = Example.objects.filter(delete=False)
        serializer = ExampleSerializers(queryset)
        return Response(serializer.data)

# Create your views here.
