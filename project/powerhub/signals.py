from .models import User, ConfirmationCode
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework import response, status
from twilio.rest import Client
import environ, os, random, logging, string
from dotenv import load_dotenv
from pathlib import Path
from setup.settings import test_settings

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
            
            account_sid = test_settings.ACCOUNT_SID
            auth_token = test_settings.AUTH_TOKEN
            
            # account_sid = 'ACf8de57181d562761a5c83fc0c34437d6'
            # auth_token = 'b2744e2b3fa9596a0596f80a49723d48'
        
            client = Client(account_sid, auth_token)
            otp_message = f'Hello! {instance.first_name}, Welcome to Queeka. Your OTP is {confirmation_code}'
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=otp_message,
                to=f'whatsapp:{contact}'
            )
        except Exception as e:
            logger.error(f"There has been an unexpected error sending OTP to {contact} \n Error: {e}", exc_info=True)

