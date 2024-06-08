from rest_framework import viewsets, permissions, response, status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from . import (
    # MODELS
    User, 
    QueekaBusiness, 
    ConfirmationCode,
    
    # SERIALIZERS
    SignUpUserSerializer,
    QueekaBusinessSerializer,
    )
from rest_framework.decorators import api_view


class SignUpUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpUserSerializer


class RegisterBusinessView(viewsets.ModelViewSet):
    """
    Register Business Accounts for Clients
    """
    queryset= QueekaBusiness.objects.select_related("owner")
    serializer_class = QueekaBusinessSerializer
    

@api_view(["GET"])
# Function to Get User Data
def retrieve_user_info(request):
    user = request.user
    try:
        user_data = get_object_or_404(User, pk=user.id)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        business_data = QueekaBusiness.objects.filter(owner=user).first()
    except QueekaBusiness.DoesNotExist:
        return None  

    data = {
        "user_data": SignUpUserSerializer(user_data).data,
        "business_data": QueekaBusinessSerializer(business_data).data if business_data else []
    }
    return JsonResponse({"status": "success", "data": data}, status=status.HTTP_200_OK)
    
# Function to verify confirmation code
@api_view(["POST"])
def verify_confirmation_code(request, **kwargs):
    # Get the submitted code from query parameters
    submitted_code = request.query_params.get("code")
    if not submitted_code:
        return JsonResponse({'error': 'Code not provided'}, status=400)

    # Get the contact from kwargs
    contact = kwargs.get("contact")
    if not contact:
        return JsonResponse({'error': 'Contact not provided'}, status=400)

    try:
        # Filter confirmation codes by user contact
        confirmation = ConfirmationCode.objects.get(user__contact=contact)
    except ConfirmationCode.DoesNotExist:
        return JsonResponse({'error': 'Confirmation code not found for this contact'}, status=404)
    
    # Check if the submitted code matches the stored code
    if str(confirmation.generated_confirmation_code) == (submitted_code):
        return JsonResponse({'status': 'success', 'message': 'Code verified successfully'})
    else:
        # print(confirmation.generated_confirmation_code)
        return JsonResponse({'status': 'failure', 'message': 'Invalid confirmation code'}, status=400)

        
@api_view(["POST"])
def resend_otp(user):
    contact = user.contact
    try:
        confirmation_code = ConfirmationCode.objects.filter(user=user).latest('created_at')
        if not confirmation_code.is_valid():
            logger.info("GENERATING NEW CONFIRMATION CODE ... ")
            confirmation_code_value = ConfirmationCode.generate_confirmation_code()
            ConfirmationCode.objects.create(user=user, generated_confirmation_code=confirmation_code_value)
        else:
            confirmation_code_value = confirmation_code.generated_confirmation_code

        logger.info("SENDING OTP")

        account_sid = test_settings.ACCOUNT_SID
        auth_token = test_settings.AUTH_TOKEN
        client = Client(account_sid, auth_token)

        otp_message = f'Hello! {user.first_name}, Welcome to Queeka. Your OTP is {confirmation_code_value}'
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=otp_message,
            to=f'whatsapp:{contact}'
        )
        logger.info("OTP sent successfully.")
        return True
    except Exception as e:
        logger.error(f"There has been an unexpected error sending OTP to {contact} \n Error: {e}", exc_info=True)
        return False