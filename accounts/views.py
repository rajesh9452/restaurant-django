# views.py
from rest_framework import status, permissions
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser , License
from .serializers import RegisterSerializer, LoginSerializer, CustomUserSerializer, LicenseSerializer


class RegisterView(APIView):
    """
    API view to register a new user with additional fields (first_name, last_name, email, phone).
    """

    def post(self, request, *args, **kwargs):
        """
        Register a new user by providing email, password, first_name, last_name, phone, and role.
        """
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Save the new user
                user = serializer.save()
                return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                # Handle duplicate email case
                if 'email' in str(e):
                    return Response({"message": "A user with this email already exists."},
                                    status=status.HTTP_400_BAD_REQUEST)
                return Response({"error": "An unexpected error occurred."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Handle validation errors from the serializer
        error_response = {field: errors for field, errors in serializer.errors.items()}
        return Response(error_response, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    API view for user login. On successful login, it returns user data with JWT token.
    """

    def post(self, request, *args, **kwargs):
        """
        Log the user in by username (email) and password.
        Return user data with JWT token.
        """
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Get the username (email) and password from the validated data
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(email=email, password=password)
            if user:
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                # Prepare the user data
                user_data = {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.phone,
                    "role": user.role.name if user.role else None,
                    "token": str(access_token),
                    "refresh_token": str(refresh)
                }

                return Response(user_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated
    def post(self, request, *args, **kwargs):
        try:
            # We can blacklist the token here or simply tell the client to discard it
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                # You can add the token to a blacklist here if you are implementing one
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the token if using blacklist feature

            return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class ProfileDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        user_data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "role": user.role.name if user.role else None
        }
        return Response(user_data, status=status.HTTP_200_OK)

class LicenseCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')  # Get user ID from the request
        start_date = request.data.get('start_date')  # Get start date from the request
        end_date = request.data.get('end_date')  # Get end date from the request
        if not user_id or not start_date or not end_date:
            return Response({"message": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(id=user_id)  # Get the user by ID
        except CustomUser.DoesNotExist:
            return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Create the license
        license = License.objects.create(
            user=user,
            start_date=start_date,
            end_date=end_date
        )
        # Serialize the license data
        license_data = {
            'user_id': license.user.id,
            'start_date': license.start_date,
            'end_date': license.end_date,
            'license_number': license.license_number
        }
        return Response(license_data, status=status.HTTP_201_CREATED)

class LicenseUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        # Assuming you are passing the license ID in the URL
        license_id = kwargs.get('license_id')
        try:
            # Fetch the license object by its ID
            license = License.objects.get(id=license_id)
        except License.DoesNotExist:
            return Response({"message": "License not found."}, status=status.HTTP_404_NOT_FOUND)

        # Only update start_date and end_date
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        if start_date:
            license.start_date = start_date
        if end_date:
            license.end_date = end_date

        license.save()

        # Return a success response
        return Response({
            "message": "License updated successfully!",
            "license": LicenseSerializer(license).data
        }, status=status.HTTP_200_OK)

class LicenseDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        # Get the license_id from the URL
        license_id = kwargs.get('license_id')
        try:
            # Fetch the license object by its ID
            license = License.objects.get(id=license_id)
        except License.DoesNotExist:
            return Response({"message": "License not found."}, status=status.HTTP_404_NOT_FOUND)

        # Delete the license object
        license.delete()

        # Return a success response
        return Response({"message": "License deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

class LicenseListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get all licenses
        licenses = License.objects.all()
        # Serialize the data
        serializer = LicenseSerializer(licenses, many=True)
        # Return the list of licenses
        return Response(serializer.data, status=status.HTTP_200_OK)