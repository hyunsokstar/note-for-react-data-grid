# Generated by Django 3.2 on 2023-04-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0030_auto_20230420_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprogress',
            name='is_success_for_cash_prize',
            field=models.BooleanField(default=False),
        ),
    ]
