# Generated by Django 3.2 on 2023-06-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_note', '0015_qnaboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnaboard',
            name='page',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
