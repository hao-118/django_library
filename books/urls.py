from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<str:isbn>/', views.book_detail, name='book_detail'),
    path('register/', register, name='register'),
]
