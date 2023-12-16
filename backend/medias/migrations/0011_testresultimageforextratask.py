# Generated by Django 3.2 on 2023-06-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_progress', '0062_testersfortestforextratask'),
        ('medias', '0010_rename_task_testresultimagefortask_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResultImageForExtraTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField()),
                ('test', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_result_images', to='project_progress.testforextratask')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
