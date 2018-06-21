from rest_framework import serializers
from app import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validate_data):
        '''
        This modules allows us to create user and serialize on api call

        Args: 
          validate_data: (str) username, (str) first_name, (str) last_name,  (str) email, (str) password

        '''
        username = validate_data.get('username')
        first_name = validate_data.get('first_name')
        last_name = validate_data.get('last_name')
        email = validate_data.get('email')
        password = validate_data.get('password')
        user = User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   password=make_password(password))
        return user


class CitizenAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CitizenAddress
        fields = ['username', 'address', 'latitude', 'longitude']

    def create(self, validate_data):
        '''

        Args: 
          validate_data: (form) with username(str), address(str),
          latitude(float), longitude(float)
        
        Returns: 
                address(str) after its created successfully
        '''
        username = validate_data.get('username')
        address = validate_data.get('address')
        latitude = validate_data.get('latitude')
        longitude = validate_data.get('longitude')
        address_ = models.CitizenAddress.objects.create(username=username,
                                   address=address,
                                   latitude=latitude,
                                   longitude=longitude)
        return address_


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payments
        fields = ['username', 'balance', 'pay_date', 'collected', 'collected_date']

class OfficeAddress(serializers.ModelSerializer):
    class Meta:
        model = models.OfficeAddress
