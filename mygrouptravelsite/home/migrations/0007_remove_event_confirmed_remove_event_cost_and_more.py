# Generated by Django 4.0.4 on 2022-04-27 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_event_cost_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='event',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='trip',
        ),
    ]
