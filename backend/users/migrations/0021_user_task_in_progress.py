# Generated by Django 3.2 on 2023-05-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_user_is_edit_mode_for_study_note_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='task_in_progress',
            field=models.CharField(default='crud 작업중', max_length=50),
        ),
    ]
