# Generated by Django 4.2.11 on 2024-04-02 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('powerhub', '0005_user_contact_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=50, unique=True)),
                ('account_id', models.CharField(max_length=35, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('business', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='powerhub.queekabusiness')),
            ],
        ),
    ]
