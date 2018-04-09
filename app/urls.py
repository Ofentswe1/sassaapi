from django.urls import path, include
from app import views

urlpatterns = [
    path('app/api/<str:username>/<str:password>/', views.Login.as_view(),
    name='login'),
    path('api/citizen/', views.RegisterCitizen.as_view(), name='citizen'),
    path('api/address/', views.CitizenAddress.as_view(), name='citizen'),
]
