# Generated by Django 4.2.11 on 2024-05-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0025_alter_address_timeframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image1',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='image2',
            field=models.URLField(),
        ),
    ]