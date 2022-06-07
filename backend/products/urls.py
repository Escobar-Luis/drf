# Keep all app urls in on place

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
    path('', views.product_create_view)
]