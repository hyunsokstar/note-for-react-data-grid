# Generated by Django 3.2 on 2023-07-06 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0066_projectprogress_is_for_today'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectprogress',
            name='is_for_today',
        ),
    ]
