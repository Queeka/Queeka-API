from .models import User, ConfirmationCode
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework import response, status
from twilio.rest import Client
import logging
import environ
import random
import string

env = environ.Env()
environ.Env.read_env()

logger = logging.getLogger(__name__)


# Signal to send OTP via Twilio WhatsApp
@receiver(post_save, sender=User)
def send_otp(sender, instance, created, **kwargs):
    if created:
        contact = instance.contact
        try:
            # Generate confirmation code
            logger.info("GENERATING CONFIRMATION CODE ... ")
            confirmation_code = ConfirmationCode.generate_confirmation_code()

            # Save the confirmation code for the user
            logger.info("CREATING CONFIRMATION CODE FOR USER")
            ConfirmationCode.objects.create(user=instance, generated_confirmation_code=confirmation_code)

            # Send OTP message via Twilio
            logger.info("SENDING OTP")
            
            account_sid = env("ACCOUNT_SID")
            auth_token = env("AUTH_TOKEN")
        
            client = Client(account_sid, auth_token)
            otp_message = f'Hello! {instance.first_name}, Welcome to Queeka. Your OTP is {confirmation_code}'
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=otp_message,
                to=f'whatsapp:{contact}'
            )
        except Exception as e:
            logger.error(f"There has been an unexpected error sending OTP to {contact} \n Error: {e}", exc_info=True)


# Function to verify confirmation code
def verify_confirmation_code(user, submitted_code):
    try:
        confirmation = ConfirmationCode.objects.get(user=user)
        if confirmation.generated_confirmation_code == submitted_code:
            confirmation.verified = True
            confirmation.save()
            return response.Response("OTP Verified Successfully", status=status.HTTP_202_ACCEPTED)
            logger.info("OTP Verified")
        else:
            return response.Response("Incorrect Confirmation Code")

    except ConfirmationCode.DoesNotExist:
        return response.Response("Confirmation Code Does Not Exist")
        logger.error("Confirmation Code Does Not Exist")
        return False

