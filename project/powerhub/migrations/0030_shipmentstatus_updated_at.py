# Generated by Django 4.2.11 on 2024-05-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0029_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentstatus',
            name='updated_at',
            field=models.TimeField(auto_now=True),
        ),
    ]