# Generated by Django 4.2.11 on 2024-05-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0028_alter_shipment_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400)),
            ],
        ),
    ]
