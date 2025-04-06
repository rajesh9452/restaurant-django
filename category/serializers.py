from django.apps import apps
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    promotions = serializers.PrimaryKeyRelatedField(
        queryset=apps.get_model('promotion', 'Promotion').objects.all(),  # Dynamically load model
        many=True,
        required=False,  # Make it optional
        allow_null=True  # Allow null values
    )

    class Meta:
        model = Category
        fields = '__all__'
