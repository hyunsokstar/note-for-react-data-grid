# Generated by Django 3.2 on 2023-09-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0030_auto_20230928_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengeresult',
            name='github_url3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='challengeresult',
            name='note_url2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='challengeresult',
            name='note_url3',
            field=models.URLField(blank=True, null=True),
        ),
    ]