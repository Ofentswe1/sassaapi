from django.urls import path, include
from app import views

urlpatterns = [
    path('app/api/<str:username>/<str:password>/', views.Login.as_view(),
    name='login'),
]
