# Generated by Django 4.2.11 on 2024-05-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0009_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DurationField(auto_created=True),
        ),
    ]
