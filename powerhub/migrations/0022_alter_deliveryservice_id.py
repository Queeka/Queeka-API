# Generated by Django 4.2.11 on 2024-05-21 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0021_shipment_delivery_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryservice',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]