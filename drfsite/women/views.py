from django.shortcuts import render
from rest_framework import  generics
from rest_framework.generics import ListAPIView

# Create your views here.
from .models import Women

from .serializers import WomenSerialazer


class WomenApiiew(generics.ListAPIView):
    queryset= Women.objects.all()
    serializer_class = WomenSerialazer


