# Generated by Django 4.0.4 on 2022-05-10 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_photos_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
