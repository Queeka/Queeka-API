from rest_framework import serializers
from . import Package, Order, QueekaBusiness
import logging

logger = logging.getLogger(__name__)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {"vendor": {"required": False}, 
                        "order_sn": {"required": False}}
        
    def create(self, validated_data):
        vendor = self.context['request'].user
        business = self.get_vendor_business(vendor)
        validated_data['vendor'] = business
        return super().create(validated_data)
    
    def get_vendor_business(self, vendor_id):
        try:
            business = QueekaBusiness.objects.get(owner=vendor_id)
        except QueekaBusiness.DoesNotExist:
            logger.error(f"Business Account Not Found for user {vendor_id}")
            raise serializers.ValidationError("You don't have a business account yet!")
        
        logger.info("Business Account Retrieved Successfully!")
        return business
    
    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['vendor'] = {"business_name": f"{instance.vendor.name}", "vendor": f"{instance.vendor.owner.first_name} {instance.vendor.owner.last_name}"}
        representation['package'] = [{"name": package.name, "size": package.size, "weight": package.weight, "type": package.type, 
                                    "recipient_address": package.address, "recipient_contact": package.recipient_contact} 
                                    for package in instance.package.all()]
        return representation


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"
        extra_kwargs = {"serial_no": {'required': False}}