from django.shortcuts import render
from rest_framework import generics
from studentapp.serializers import studentserializer
from studentapp.models import studentdb

# Create your views here.

class studentcreate(generics.ListCreateAPIView):
    queryset = studentdb.objects.all()
    serializer_class = studentserializer

class studentalldetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = studentdb.objects.all()
    serializer_class = studentserializer
