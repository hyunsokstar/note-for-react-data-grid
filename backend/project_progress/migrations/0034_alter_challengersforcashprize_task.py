# Generated by Django 3.2 on 2023-04-21 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0033_challengersforcashprize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengersforcashprize',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challegers_for_cach_prize', to='project_progress.projectprogress'),
        ),
    ]