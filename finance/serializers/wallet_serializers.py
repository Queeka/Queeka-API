from . import BusinessWallet
from rest_framework import serializers

class BusinessWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessWallet
        fields = ("business", "nuban", "name", "balance")
        
    def validate(self, attrs):
        balance = attrs.get("balance")
        if float(balance) < 0.00:
            raise serializers.ErrorDetail("You can't credit your account with less than NGN 100")
        return attrs
    