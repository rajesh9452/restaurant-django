# menu/urls.py
from django.urls import path
from .views import PromotionListView, PromotionDeleteView, PromotionCreateView, PromotionUpdateView, PromotionDetailView

urlpatterns = [
    path('promotions', PromotionListView.as_view(), name='promotion-list'),
    path('promotions/create', PromotionCreateView.as_view(), name='promotion-create'),
    path('promotions/<int:pk>', PromotionDetailView.as_view(), name='promotion-detail'),
    path('promotions/<int:pk>/update', PromotionUpdateView.as_view(), name='promotion-update'),
    path('promotions/<int:pk>/delete', PromotionDeleteView.as_view(), name='promotion-delete'),
]
