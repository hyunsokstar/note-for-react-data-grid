# Generated by Django 3.2 on 2023-09-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0012_rename_user_evaluationresult_challenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
