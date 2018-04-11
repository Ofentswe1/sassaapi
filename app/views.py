from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from app import models
from app import serializers as sz

# Create your views here.
class Login(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                username = user.username
                user = authenticate(username=username, password=password)
                login(request, user)
                details = User.objects.get(username=username)
                serialized_obj = serializers.serialize('json', [details, ])
                return HttpResponse(serialized_obj)
            else:
                return HttpResponse('{"messages":"Wrong password"}')
        except User.DoesNotExist:
            return HttpResponse('{"message":"username and password incorrect"}')

class RegisterCitizen(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = sz.UserSerializer

class CitizenAddress(generics.ListCreateAPIView):
    queryset = models.CitizenAddress.objects.all()
    serializer_class = sz.CitizenAddressSerializer

class OfficeAddress(generics.ListAPIView):
    queryset = models.OfficeAddress.objects.all()
    serializer_class = sz.PaymentsSerializer

class Payments(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = models.Payments.objects.all()
        serializer_class = sz.PaymentsSerializer

class Beneficiaries(generics.ListAPIView):
    query_set = User.objects.all()
    serializer_class = None
