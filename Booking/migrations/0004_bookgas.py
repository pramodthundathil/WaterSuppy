# Generated by Django 5.0.2 on 2024-03-08 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_alter_agencystock_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateField(auto_now_add=True)),
                ('approval_status', models.BooleanField(default=False)),
                ('status', models.CharField(default='Booked Not Approved', max_length=30)),
                ('deliverydate', models.DateField(null=True)),
                ('Gas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.agencystock')),
            ],
        ),
    ]
