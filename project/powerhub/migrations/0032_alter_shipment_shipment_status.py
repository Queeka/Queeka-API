# Generated by Django 4.2.11 on 2024-05-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0031_remove_shipmentstatus_shipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipment_status',
            field=models.ManyToManyField(null=True, related_name='statuses', to='powerhub.shipmentstatus'),
        ),
    ]