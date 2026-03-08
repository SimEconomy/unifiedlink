from rest_framework import serializers
from .models import CRMEntity

class CRMEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMEntity
        fields = '__all__'