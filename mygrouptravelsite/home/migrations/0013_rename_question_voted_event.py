# Generated by Django 4.0.4 on 2022-05-04 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_voted_event_voters_event_votes_voted_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voted',
            old_name='question',
            new_name='event',
        ),
    ]
