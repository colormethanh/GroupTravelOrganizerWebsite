# Generated by Django 4.0.4 on 2022-05-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_trip_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='A cool event for a cool group of people :)', max_length=200),
        ),
    ]
