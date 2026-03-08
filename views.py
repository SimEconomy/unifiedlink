from django.http import JsonResponse
from .models import CRMEntity
from rest_framework import generics

class EntityList(generics.ListCreateAPIView):
    queryset = CRMEntity.objects.all()
    serializer_class = CRMEntitySerializer  # Assuming a serializer has been defined

class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CRMEntity.objects.all()
    serializer_class = CRMEntitySerializer
