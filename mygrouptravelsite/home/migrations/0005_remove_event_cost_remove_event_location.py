# Generated by Django 4.0.4 on 2022-04-27 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_event_cost_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]
