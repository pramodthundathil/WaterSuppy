# Generated by Django 5.0.2 on 2024-03-08 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0005_bookgas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencystock',
            name='Gas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking.gascylinder'),
        ),
    ]