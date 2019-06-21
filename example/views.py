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
        serializer = ExampleSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ExampleDetail(APIView):
    def get_object(self, id):
        try:
            return Example.objects.get(pk=id, delete=False)
        except Example.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404:
            serializer = ExampleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(example)

    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != 404: 
            serializer = ExampleSerializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(example, status = status.HTTP_400_BAD_REQUEST)