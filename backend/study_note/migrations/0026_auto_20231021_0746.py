# Generated by Django 3.2 on 2023-10-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_note', '0025_commentforfaqboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='cowriterforstudynote',
            name='is_tasking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cowriterforstudynote',
            name='task_description',
            field=models.BooleanField(default=False),
        ),
    ]
