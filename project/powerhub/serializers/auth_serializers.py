from . import User, Waitlist, QueekaBusiness
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import re


class SignUpUserSerializer(serializers.ModelSerializer):
    contact = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "contact", "password", "profile_image"]
        extra_kwargs = {"email": {"required": False}}
        
    def validate_password(self, value):
        # Password Security
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', value):
            raise serializers.ValidationError({"error": "Passwords must include at least one special symbol, one number, one lowercase letter, and one uppercase letter."})
        if len(value) <= 5:
            raise serializers.ValidationError({"error": "Passwords must be more than 5 characters."})
        return value
    
    def create(self, validated_data):
        sme = User(**validated_data)
        sme.tier_1=True
        sme.save()
        return sme



class SignUpSMESerializer(serializers.ModelSerializer):
    contact = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "contact", "password", "profile_image"]
        extra_kwargs = {"email": {"required": False}}
        
    def validate_password(self, value):
        # Password Security
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', value):
            raise serializers.ValidationError({"error": "Passwords must include at least one special symbol, one number, one lowercase letter, and one uppercase letter."})
        if len(value) <= 5:
            raise serializers.ValidationError({"error": "Passwords must be more than 5 characters."})
        return value
    
    def create(self, validated_data):
        sme = User(**validated_data)
        sme.tier_3=True
        sme.save()
        return sme



class QueekaBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueekaBusiness
        fields = ["id", "owner", "name", "address", "city", "country", "business_sn"]
        read_only_fields = ["business_sn"]
    
    def to_representation(self, instance):
        representation = super(QueekaBusinessSerializer, self).to_representation(instance)
        representation['owner'] = {"id": instance.owner.id, "full_name": f"{instance.owner.first_name} {instance.owner.last_name}"}
        return representation
    
    def create(self, validated_data):
        sme = QueekaBusiness(**validated_data)
        sme.tier_2=True
        sme.save()
        return sme