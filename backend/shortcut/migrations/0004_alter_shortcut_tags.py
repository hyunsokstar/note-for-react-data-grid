# Generated by Django 3.2 on 2023-04-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcut', '0003_auto_20230410_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcut',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='shortcuts', to='shortcut.Tags'),
        ),
    ]