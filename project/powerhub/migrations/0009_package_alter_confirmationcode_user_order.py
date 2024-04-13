# Generated by Django 4.2.11 on 2024-04-13 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0008_alter_confirmationcode_generated_confirmation_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('quantity', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('GR', 'Groceries'), ('CA', 'Clothing and Apparel'), ('EL', 'Electronics'), ('BM', 'Books and Media'), ('HBP', 'Health & Beauty Products'), ('HGF', 'Home Goods and Furniture'), ('TG', 'Toys and Games'), ('SOE', 'Sports and Outdoor Equipment'), ('PS', 'Pet Supplies'), ('OS', 'Office Supplies'), ('SFB', 'Specialty Foods and Beverages'), ('PMS', 'Pharmaceuticals and Medical Supplies'), ('APA', 'Automotive Parts and Accessories'), ('GF', 'Gifts and Flowers')], max_length=3)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('size', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=300)),
                ('recipient_contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='confirmationcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_sn', models.CharField(max_length=5, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('delivery_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('type', models.CharField(choices=[('ED', 'Express'), ('NM', 'Normal')], max_length=2)),
                ('message', models.TextField()),
                ('package', models.ManyToManyField(related_name='items', to='powerhub.package')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powerhub.queekabusiness')),
            ],
        ),
    ]