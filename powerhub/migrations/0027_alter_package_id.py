# Generated by Django 4.2.11 on 2024-05-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0026_alter_package_image1_alter_package_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]