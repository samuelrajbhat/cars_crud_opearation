from rest_framework import viewsets
from django.shortcuts import get_list_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CarsViewset(APIView):
    def get(self, request, id = None):
        if id:
            item = models.Cars.objects.get(id = id)
            serializer = serializers.CarsSeralizers(item)
            return Response({"status" : "success", "data": serializer.data}, status= status.HTTP_200_OK)
        items = models.Cars.objects.all()
        serializer = serializers.CarsSeralizers(items, many= True)
        return Response({"status": "success", "data": serializer.data}, status= status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.CarsSeralizers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status= status.HTTP_200_OK)
        else:
            return Response({"status" : "error", "data": serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
 