# Generated by Django 4.2.11 on 2024-04-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0010_order_delivery_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]