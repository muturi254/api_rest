from django.shortcuts import render
from rest_framework import generics

from e_api.models import Category, Book, Product
from e_api.serializers import ProductSerializer, CategorySerializer, BookSerializer
# Create your views here.
class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer