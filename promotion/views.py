from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Promotion
from .serializers import PromotionSerializer


# List all promotions
# List all promotions
class PromotionListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create a new promotion
class PromotionCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = PromotionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve a single promotion by ID
class PromotionDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            promotion = Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            return Response({"detail": "Promotion not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PromotionSerializer(promotion)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Update an existing promotion
class PromotionUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, pk, *args, **kwargs):
        try:
            promotion = Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            return Response({"message": "Promotion not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PromotionSerializer(promotion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a promotion
class PromotionDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            promotion = Promotion.objects.get(pk=pk)
        except Promotion.DoesNotExist:
            return Response({"message": "Promotion not found."}, status=status.HTTP_404_NOT_FOUND)

        promotion.delete()
        return Response({"message": "Promotion deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
