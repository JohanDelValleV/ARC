from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Rfid.models import Rfid
from Rfid.serializer import RfidSerializers

class RfidList(APIView):
    def get(self, request, format=None):
        queryset = Rfid.objects.filter(delete=False)
        serializer = RfidSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RfidSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas["id"])
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class RfidDetail(APIView):
    def get_object(self, id):
        try:
            return Rfid.objects.get(id_rfid=id)
        except:
            return 404

    def get(self, request, id , format=None):
        rfid = self.get_object(id)
        if rfid != 404:
            serializer = RfidSerializers(rfid)
            return Response(serializer.data)
        else:
            return Response(rfid)

    def put(self, request, id, format=None):
        rfid = self.get_object(id)
        if rfid != 404:
            serializer = RfidSerializers(rfid, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(rfid, status=status.HTTP_404_BAD_REQUEST)