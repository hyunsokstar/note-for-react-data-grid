# Generated by Django 3.2 on 2023-03-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20230301_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_level',
            field=models.IntegerField(default=1),
        ),
    ]