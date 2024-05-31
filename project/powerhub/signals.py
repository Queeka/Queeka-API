from .models import User, ConfirmationCode, NotificationSystem, ShipmentStatus, Shipment
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework import response, status
from twilio.rest import Client
import environ, os, random, logging, string, requests
from dotenv import load_dotenv
from pathlib import Path
from setup.settings import test_settings
from django.shortcuts import get_object_or_404


# Signal to send OTP via Twilio WhatsApp
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def handle_welcome_notification_and_otp(sender, instance, created, **kwargs):
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
        
            client = Client(account_sid, auth_token)
            otp_message = f'Hello! {instance.first_name}, Welcome to Queeka. Your OTP is {confirmation_code}'
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=otp_message,
                to=f'whatsapp:{contact}'
            )
        except Exception as e:
            logger.error(f"There has been an unexpected error sending OTP to {contact} \n Error: {e}", exc_info=True)

        # Notification Signals
        try:
            NotificationSystem.objects.create(
                user=instance,
                title="Welcome to Queeka!",
                text=(
                    "Hello and welcome to Queeka!\n"
                    "I'm Israel Abiona, the CEO and Co-Founder of Queeka.\n"
                    "Our journey begins with you and for you. Queeka aims to transform\n"
                    "logistics management in Nigeria and across Africa.\n"
                    "We're thrilled to have you join us on this exciting venture. We know it's going to be a long journey,\n"
                    "but we're confident that you'll stay with us through it all. Thank you for joining us! Let's achieve great things together!"
                )
            )
            logger.info("Message Sent Successfully")
        except Exception as e:
            logger.error(f"Could not send notification to {instance.contact} \n Error: {e}", exc_info=True)
            return response.Response("Error Creating Notification!")
        
        
@receiver(post_save, sender=Shipment)
def handle_initiate_shipment_status_process(sender, instance, created, **kwargs):
    if created:
        vendor = instance.vendor
        
        user = get_object_or_404(User, id=vendor.owner.id)
        # Send Notification
        try:
            NotificationSystem.objects.create(
                user = user,
                title="Shipment",
                text=(
                    "Your Shipment request has been recieved and is been processed \n"
                    f"A courier from {instance.delivery_service.service} will get to you shortly!"
                    )
            )
            
            ShipmentStatus.objects.create(
                shipment=instance,
                status="PR"
            )
        except Exception as e:
            # print(str(e))
            logger.error(str(e))
            return response.Response({"status": "error", "data": str(e)})