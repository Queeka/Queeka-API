# Generated by Django 4.2.11 on 2024-05-13 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0004_address_deliveryrecipient_remove_package_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('DHL', 'DHL'), ('GIGL', 'GIGL'), ('Kwik', 'Kwik'), ('RedStar', 'RedStar'), ('Glovo', 'Glovo'), ('Chowdeck', 'Chowdeck'), ('TopShip', 'TopShip')], max_length=8)),
                ('logo', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PackageDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=250)),
                ('recipient_contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PackagePickUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=250)),
                ('recipient_contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='address',
        ),
        migrations.DeleteModel(
            name='DeliveryRecipient',
        ),
        migrations.RemoveField(
            model_name='address',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='delivery_service',
        ),
        migrations.AddField(
            model_name='package',
            name='is_insured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='is_returnable',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
        migrations.AddField(
            model_name='packagepickup',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerhub.address'),
        ),
        migrations.AddField(
            model_name='packagepickup',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='powerhub.package'),
        ),
        migrations.AddField(
            model_name='packagedelivery',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerhub.address'),
        ),
        migrations.AddField(
            model_name='packagedelivery',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='powerhub.package'),
        ),
    ]
