# Generated by Django 5.0.2 on 2024-04-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewexperience',
            name='github',
            field=models.CharField(max_length=300),
        ),
    ]
