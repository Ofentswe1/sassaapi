from django.urls import path, include
from app import views

urlpatterns = [
    path('app/api/<str:username>/<str:password>/', views.Login.as_view(),
    name='login'),
    path('api/citizen/', views.RegisterCitizen.as_view(), name='citizen'),
    path('api/address/<str:username>/', views.CitizenAddress.as_view(), name='address'),
    path('api/payments/<int:username>/', views.Payments.as_view(), name='payments'),
    path('api/officeaddress/', views.OfficeAddress.as_view(), name='OfficeAddress'),
    path('home/', views.HomePage.as_view(), name='home'),
]
