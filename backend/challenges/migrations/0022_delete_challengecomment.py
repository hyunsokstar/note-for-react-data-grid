# Generated by Django 3.2 on 2023-09-25 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0021_challengecomment_challenge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChallengeComment',
        ),
    ]
