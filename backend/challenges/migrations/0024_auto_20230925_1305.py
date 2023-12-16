# Generated by Django 3.2 on 2023-09-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0023_challengecomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challengecomment',
            old_name='commenter',
            new_name='writer',
        ),
        migrations.AlterField(
            model_name='challengecomment',
            name='commenter_classfication',
            field=models.CharField(choices=[('commenter', 'Commenter'), ('challenger', 'Challenger'), ('participant', 'Participant')], default='commenter', max_length=20),
        ),
    ]
