# urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileDetailsView, LicenseCreateView, LicenseUpdateView, LicenseDeleteView, LicenseListView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileDetailsView.as_view(), name='profile_details'),
    path('license/create', LicenseCreateView.as_view(), name='create_license'),
    path('license/update/<int:license_id>', LicenseUpdateView.as_view(), name='update_license'),
    path('license/delete/<int:license_id>', LicenseDeleteView.as_view(), name='delete_license'),
    path('license/list', LicenseListView.as_view(), name='license-list'),
]
