# Generated by Django 4.0.4 on 2022-05-09 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_photos_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_photos', to='home.event'),
        ),
    ]
