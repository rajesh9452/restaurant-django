from rest_framework import viewsets, serializers
from .models import Promotion

# Serializer for Promotion
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'
