# menu/urls.py
from django.urls import path
from .views import MenuListView, MenuCreateView, MenuDetailView, MenuUpdateView, MenuDeleteView

urlpatterns = [
    path('menus', MenuListView.as_view(), name='menu-list'),  # GET all menus
    path('menus/create', MenuCreateView.as_view(), name='menu-create'),  # POST create menu
    path('menus/<int:pk>', MenuDetailView.as_view(), name='menu-detail'),  # GET a specific menu
    path('menus/<int:pk>/update', MenuUpdateView.as_view(), name='menu-update'),  # PUT update menu
    path('menus/<int:pk>/delete', MenuDeleteView.as_view(), name='menu-delete'),  # DELETE menu
]
