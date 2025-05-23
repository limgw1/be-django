# Generated by Django 5.2.1 on 2025-05-12 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0004_alter_task_parent_id_alter_task_project_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='user_id',
        ),
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_name',
            field=models.CharField(default='Lose Weight', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='priority',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='GoalHistory',
        ),
    ]
