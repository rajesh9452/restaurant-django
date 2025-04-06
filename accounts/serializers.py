# serializers.py
from rest_framework import serializers
from .models import CustomUser, Role, License
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = CustomUser
        fields = ['id','email', 'first_name', 'last_name', 'phone', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'role')  # No username field

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  # Hash the password before saving
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class LicenseSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()  # Custom field to get user's full name
    class Meta:
        model = License
        fields = ['id', 'user', 'user_name', 'start_date', 'end_date', 'license_number']
        read_only_fields = ['license_number']  # The license number is automatically generated

    def get_user_name(self, obj):
        # Return the user's full name (first_name + last_name)
        return f"{obj.user.first_name} {obj.user.last_name}" if obj.user else None

    def update(self, instance, validated_data):
        # Only update start_date and end_date, leave license_number intact
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
