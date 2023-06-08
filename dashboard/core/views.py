from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Accident
from django.http import JsonResponse
from . services import AccidentsService
from . serializers import AccidentSerializer
import requests


@api_view(['POST'])
def create_accident(request):
    data = request.data
    service = AccidentsService(data.get('year'))
    data = service.accidents()
    serializer = AccidentSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)






#@api_view(['GET'])
#def get_accidents(requet):
#    accidents = Accident.objects.get()





# Create your views here.
