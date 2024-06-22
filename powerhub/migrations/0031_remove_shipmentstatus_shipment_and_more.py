# Generated by Django 4.2.11 on 2024-05-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0030_shipmentstatus_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipmentstatus',
            name='shipment',
        ),
        migrations.AddField(
            model_name='shipment',
            name='shipment_status',
            field=models.ManyToManyField(related_name='statuses', to='powerhub.shipmentstatus'),
        ),
    ]
