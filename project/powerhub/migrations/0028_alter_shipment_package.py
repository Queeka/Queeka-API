# Generated by Django 4.2.11 on 2024-05-22 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0027_alter_package_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='package',
            field=models.ManyToManyField(related_name='shipments', to='powerhub.package'),
        ),
    ]