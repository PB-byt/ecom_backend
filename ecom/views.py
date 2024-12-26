from django.shortcuts import render
# Create your views here.
# api endpoints will be defined here and also we will use serializer classes , made in serializer.py
from django.http import HttpResponse # <-- this is normal http response , one that we will use is Response from rest_framework
from .models import Product,Pictures
from .serializer import Productserializer,Pictureserializer#,ProductWithFirstPictureSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def get_data(request):
    stuffs = Product.objects.all()
    serialized = Productserializer(stuffs,many=True)
    return Response(serialized.data,status=status.HTTP_200_OK)

@api_view(['GET'])
# @renderer_classes([JSONRenderer])
def get_pics(request,obj):# function will be called via button with it's id(obj)
    try:
      prod = Product.objects.get(id=obj)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
    pics = prod.photos.all()
    sed = Pictureserializer(pics,many=True)
    return Response(sed.data,status=status.HTTP_200_OK)
    # else:
    #     return Response("product has no phots",status=status.HTTP_404_NOT_FOUND)
# @api_view(['GET'])
# def get_full_data(request):
#     pr = Product.objects.all()
#     sed = ProductWithFirstPictureSerializer(pr,many = True)
#     return Response(sed.data,status=status.HTTP_200_OK)

























def home(request):
    return HttpResponse("greate things take time... be patient")

