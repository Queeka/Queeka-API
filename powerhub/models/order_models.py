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
    id = models.CharField(max_length=8, primary_key=True)
    serial_no = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    image1 = models.URLField()
    image2 = models.URLField()
    quantity = models.PositiveIntegerField()
    type = models.CharField(max_length=3, choices=PACKAGE_TYPE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    size = models.CharField(max_length=10)
    pickup = models.ForeignKey('powerhub.Address', on_delete=models.SET_NULL, null=True)
    is_insured = models.BooleanField(default=False)
    is_returnable = models.BooleanField(default=False)
    value = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = "PK-" + "".join(random.choices(string.digits, k=5))
        if not self.serial_no:
            generated_serial_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
            self.serial_no = generated_serial_no
        super(Package, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.serial_no
    


class Address(models.Model):
    address = models.CharField(max_length=300)
    recipient_name = models.CharField(max_length=350, null=True)
    recipient_contact = models.CharField(max_length=15, null=True)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, default="Nigeria")
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    timeframe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DeliveryService(models.Model):
    SERVICE = (
        ("DHL", "DHL"),
        ("GIGL", "GIGL"),
        ("Kwik", "Kwik"),
        ("RedStar", "RedStar"),
        ("Glovo", "Glovo"),
        ("Chowdeck", "Chowdeck"),
        ("TopShip", "TopShip")
    )
    id = models.CharField(max_length=5, primary_key=True)
    service = models.CharField(max_length=8, choices=SERVICE)
    logo = models.URLField(null=False)
    is_active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = "".join(random.choices(string.digits, k=5))
        super(DeliveryService, self).save(*args, **kwargs)

    def __str__(self):
        return self.service


class Shipment(models.Model):
    TYPE = (
        ("ED", "Express"),
        ("NM", "Normal")
    )
    
    VEHICLE_TYPE = (
        ("BIKE", "BIKE"),
        ("CAR", "CAR"),
        ("VAN", "VAN"),
        ("TRUCK", "TRUCK")
    )

    vendor = models.ForeignKey(QueekaBusiness, on_delete=models.CASCADE)
    delivery_service = models.ForeignKey(DeliveryService, on_delete=models.SET_NULL, null=True)
    tracking_id = models.CharField(max_length=7, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipment_sn = models.CharField(max_length=5, unique=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    delivery_fee = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    type = models.CharField(max_length=2, choices=TYPE)
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPE, null=True)
    package = models.ManyToManyField(Package, related_name="shipments")
    status = models.ManyToManyField('powerhub.ShipmentStatus', related_name="statuses")
    message = models.TextField()

    def __str__(self):
        return self.tracking_id

    def save(self, *args, **kwargs):
        if not self.shipment_sn:
            self.shipment_sn = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if not self.tracking_id:
            self.tracking_id = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        super(Shipment, self).save(*args, **kwargs)



class ShipmentStatus(models.Model):
    STATUS = (
        ("PR", "Processing"),
        ("CA", "Courier Arrived"),
        ("PU", "Picked Up"),
        ("EN", "Enroute"),
        ("DL", "Delayed"),
        ("DEL", "Delivered"),
        ("CANC", "Cancelled")
    )
    status = models.CharField(max_length=4, choices=STATUS, default="PR")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.status} at {self.timestamp}"