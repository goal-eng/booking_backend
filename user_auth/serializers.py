from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from . import models
from datetime import date
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




class UserRegisterSerializer(serializers.ModelSerializer):
    queryset=models.CustomUser.objects.all()
    email = serializers.EmailField(
            required=False ,validators=[UniqueValidator(queryset=queryset)]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.CustomUser
        fields = ("email","password", "password2","name")
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'required': True, 'allow_blank': False},
            'password2': {'required': True, 'allow_blank': False},
            }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        name = validated_data.pop("name", None)
        user = models.CustomUser.objects.create(
            email=email, 
            password=make_password(password),
            name=name,
        )
        print("YTHFUYGUYGH",user)
        return user

    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()
        return instance



class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("email","name","role")