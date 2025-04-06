# menu/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class MenuListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get all menus
        menus = Menu.objects.all()
        # Serialize the data
        serializer = MenuSerializer(menus, many=True, context={'request': request})
        # Return the list of menus
        return Response(serializer.data, status=status.HTTP_200_OK)



class MenuCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # Handle image uploads

    def post(self, request, *args, **kwargs):
        serializer = MenuSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            # Get the menu by ID
            menu = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"message": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the menu
        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

# menu/views.py
class MenuUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)  # Handle file uploads

    def put(self, request, pk, *args, **kwargs):
        try:
            # Get the menu by ID
            menu = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"message": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)

        # Deserialize the data and update the menu
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# menu/views.py
class MenuDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            # Get the menu by ID
            menu = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"message": "Menu not found."}, status=status.HTTP_404_NOT_FOUND)

        # Delete the menu
        menu.delete()
        return Response({"message": "Menu deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
