from rest_framework import serializers
from . import Package, Shipment, ShipmentStatus, QueekaBusiness, DeliveryService, Address
import logging

logger = logging.getLogger(__name__)

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"
        extra_kwargs = {"vendor": {"required": False}, 
                        "shipment_sn": {"required": False},
                        "status": {"required":False}
                        }
        read_only_fields = ("tracking_id",)
        
    def create(self, validated_data):
        vendor = self.context['request'].user
        business = self.get_vendor_business(vendor)
        validated_data['vendor'] = business
        # validated_data["status"] = "PR"
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
        representation = super(ShipmentSerializer, self).to_representation(instance)
        representation['vendor'] = {"business_name": f"{instance.vendor.name}", "vendor": f"{instance.vendor.owner.first_name} {instance.vendor.owner.last_name}"}
        representation['package'] = [{"name": package.name, "size": package.size, "weight": package.weight, "type": package.type, 
                                    "recipient_address": package.pickup.address, "recipient_contact": package.pickup.recipient_contact, "recipient_name": package.pickup.recipient_name, "state": package.pickup.state, "city": package.pickup.city, "country": package.pickup.country } for package in instance.package.all()]
        representation['status'] = [{"status": status.status, "timestamp": status.timestamp.strftime("%H:%M:%p")} for status in instance.status.all()]
        representation['delivery_service'] = instance.delivery_service.service
        return representation


class ShipmentStatusSerializer(serializers.ModelSerializer):
    shipment = ShipmentSerializer()

    class Meta:
        model = ShipmentStatus
        fields = "__all__"



# class PackageDeliverySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackageDelivery
#         fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'recipient_name', 'state', 'city', 'country', 'longitude', 'latitude', 'timeframe']


class PackageSerializer(serializers.ModelSerializer):
    pickup = AddressSerializer()

    class Meta:
        model = Package
        fields = [
            'id', 'serial_no', 'name', 'image1', 'image2', 'quantity', 'type',
            'weight', 'size', 'pickup', 'is_insured', 'is_returnable', 'value'
        ]
        read_only_fields = ("id", "serial_no",)
        extra_kwargs = {"id": {"required": False}, "serial_no": {"required":False}}

    def create(self, validated_data):
        pickup_data = validated_data.pop('pickup')
        address_instance = Address.objects.create(**pickup_data)
        package_instance = Package.objects.create(pickup=address_instance, **validated_data)
        return package_instance
    

class DeliveryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryService
        fields = "__all__"
        read_only_fields = ("id",)