from django.db import models
from . import User, QueekaBusiness
import uuid, random, string


class Package(models.Model):
    PACKAGE_TYPE = (
        ("GR", "Groceries"),
        ("CA", "Clothing and Apparel"),
        ("EL", "Electronics"),
        ("BM", "Books and Media"),
        ("HBP", "Health & Beauty Products"),
        ("HGF", "Home Goods and Furniture"),
        ("TG", "Toys and Games"), 
        ("SOE", "Sports and Outdoor Equipment"),
        ("PS", "Pet Supplies"),
        ("OS", "Office Supplies"),
        ("SFB", "Specialty Foods and Beverages"), 
        ("PMS", "Pharmaceuticals and Medical Supplies"),
        ("APA", "Automotive Parts and Accessories"),
        ("GF", "Gifts and Flowers")
    )
    serial_no = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    image1 = models.ImageField()
    image2 = models.ImageField()
    quantity = models.PositiveIntegerField()
    type = models.CharField(max_length=3, choices=PACKAGE_TYPE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    size = models.CharField(max_length=10)
    pickup = models.ForeignKey('powerhub.Address', on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        if not self.serial_no:
            generated_serial_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
            self.serial_no = generated_serial_no
        super(Package, self).save(*args, **kwargs)


class Address(models.Model):
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=15)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    timeframe = models.DateTimeField()
    name = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name
    

class Delivery(models.Model):
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    is_insured = models.BooleanField(default=False)
    package_is_returnable = models.BooleanField(default=False)
    
    
    
class DeliveryRecipient(models.Model):
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=15)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    timeframe = models.DateTimeField()
    name = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name

class Shipment(models.Model):
    TYPE = (
        ("ED", "Express"),
        ("NM", "Normal")
    )
    
    DELIVERY_SERVICE = (
        ("DHL", "DHL"),
        ("GIGL", "GIGL"),
        ("Kwik", "Kwik"),
        ("RedStar", "RedStar"),
        ("Glovo", "Glovo"),
        ("Chowdeck", "Chowdeck")
    )
    
    DELIVERY_STATUS = (
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("In-Transit", "In-Transit"),
        ("Cancelled", "Cancelled")
    )
    
    vendor = models.ForeignKey(QueekaBusiness, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipment_sn = models.CharField(max_length=5, unique=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    delivery_fee = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    delivery_service = models.CharField(max_length=8, choices=DELIVERY_SERVICE)
    delivery_status = models.CharField(max_length=10, choices=DELIVERY_STATUS, default="Pending")
    type = models.CharField(max_length=2, choices=TYPE)
    package = models.ManyToManyField(Package, related_name="items")
    message = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.shipment_sn:
            self.shipment_sn = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        super(Shipment, self).save(*args, **kwargs)