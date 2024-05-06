from . import BusinessWallet
from rest_framework import serializers

class BusinessWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessWallet
        fields = ("business", "nuban", "name", "balance")
        
    def validate(self, attrs):
        balance = attrs.get("balance")
        if float(balance) < 0.00:
            raise serializers.ErrorDetail("You can credit you account with less that 100 naira")
        return attrs
    