from . import User, Waitlist, QueekaBusiness, ConfirmationCode
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import re, logging


logger = logging.getLogger(__name__)


class BaseSignUpSerializer(serializers.ModelSerializer):
    contact = serializers.CharField(required=False)
    password = serializers.CharField(required=False, write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "contact", "password", "profile_image"]
        extra_kwargs = {"email": {"required": False}}
        
    def validate_password(self, value):
        # Password Security
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$', value):
            raise serializers.ValidationError("Passwords must include at least one special symbol, one number, one lowercase letter, and one uppercase letter.")
        if len(value) <= 5:
            raise serializers.ValidationError("Passwords must be more than 5 characters.")
        return value


class SignUpUserSerializer(BaseSignUpSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.tier_1 = True
        user.save()
        return user


class SignUpSMESerializer(BaseSignUpSerializer):
    def create(self, validated_data):
        sme = User(**validated_data)
        sme.tier_2 = True
        sme.save()
        
        try:
            logger.info("GENERATING CONFIRMATION CODE ... ")
            confirmation_code = ConfirmationCode.generate_confirmation_code()

            # Save the confirmation code for the user
            logger.info("CREATING CONFIRMATION CODE FOR USER")
            ConfirmationCode.objects.create(user=sme, generated_confirmation_code=confirmation_code)
        except Exception as e:
            logger.error(str(e))
            raise serializers.ValidationError("Something broke! Please hold on, we're working on it.")
        return sme
    
    def to_representation(self, instance):
        representation = super(SignUpSMESerializer, self).to_representation(instance)
        representation['otp'] = self.get_my_otp(instance.id)
        return representation
        
    def get_my_otp(self, user):
        try:
            otp = ConfirmationCode.objects.get(user=user).generated_confirmation_code
        except ConfirmationCode.DoesNotExist:
            otp = None
            logger.error(f"Damn! Help me out chief I couldn't generate an OTP for this user: {user}")
        return otp


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