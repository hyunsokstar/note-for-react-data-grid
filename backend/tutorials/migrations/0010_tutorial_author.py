# Generated by Django 3.2 on 2023-03-07 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorials', '0009_alter_tutorial_frontend_framework_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
