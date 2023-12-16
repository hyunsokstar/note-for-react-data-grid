# Generated by Django 3.2 on 2023-03-23 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0003_projectprogress_in_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprogress',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='projectprogress',
            name='started_at_utc',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]