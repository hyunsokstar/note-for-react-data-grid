# Generated by Django 3.2 on 2023-04-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0027_projectprogress_score_by_tester'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprogress',
            name='cash_prize',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectprogress',
            name='is_urgent_request',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
