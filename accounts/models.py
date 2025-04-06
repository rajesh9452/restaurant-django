from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# from django.contrib.auth import get_user_model
#
# User = get_user_model()

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    username = None  # Disable the username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    phone = models.CharField(max_length=15, null=True, blank=True)  # Add phone field
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name="users")

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']  # Add other required fields

    def __str__(self):
        return self.email

class License(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='licenses')  # Removed default=None
    start_date = models.DateField()
    end_date = models.DateField()
    license_number = models.CharField(max_length=20, unique=True, editable=False)

    def generate_license_number(self):
        """
        Automatically generate a license number using the user's ID and current timestamp.
        """
        # You can modify the license number generation logic as per your requirement
        timestamp = timezone.now().strftime('%Y%m%d')
        return f"LIC-{self.user.id}-{timestamp}"

    def save(self, *args, **kwargs):
        if not self.license_number:
            # Generate the license number if it's not set
            self.license_number = self.generate_license_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"License {self.license_number} for {self.user.email}"
