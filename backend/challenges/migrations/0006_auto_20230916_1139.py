# Generated by Django 3.2 on 2023-09-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_alter_challenger_evaluation_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationresult',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='evaluationresult',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='evaluationresult',
            name='evaluator',
        ),
        migrations.RemoveField(
            model_name='evaluationresult',
            name='participant',
        ),
        migrations.AlterField(
            model_name='evaluationresult',
            name='result',
            field=models.CharField(choices=[('Undecided', '미결정'), ('Pass', 'Pass'), ('Fail', 'Fail')], default='Undecided', max_length=20),
        ),
    ]
