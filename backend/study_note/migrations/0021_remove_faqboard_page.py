# Generated by Django 3.2 on 2023-08-28 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_note', '0020_auto_20230827_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqboard',
            name='page',
        ),
    ]
