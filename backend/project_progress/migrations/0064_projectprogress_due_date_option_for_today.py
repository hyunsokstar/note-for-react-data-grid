# Generated by Django 3.2 on 2023-07-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0063_alter_projectprogress_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectprogress',
            name='due_date_option_for_today',
            field=models.CharField(choices=[('until-noon', '오전까지'), ('until-evening', '오후까지'), ('until-afternoon', '오후 이후까지')], default='until-noon', max_length=20),
        ),
    ]