# Generated by Django 4.0.4 on 2022-04-27 02:37

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_trip_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(validators=[home.models.date_validator]),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(validators=[home.models.date_validator]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateField(validators=[home.models.date_validator]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateField(validators=[home.models.date_validator]),
        ),
    ]
