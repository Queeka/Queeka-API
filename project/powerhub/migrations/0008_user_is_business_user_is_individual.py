# Generated by Django 4.2.11 on 2024-05-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0007_confirmationcode_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_business',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_individual',
            field=models.BooleanField(default=False),
        ),
    ]
