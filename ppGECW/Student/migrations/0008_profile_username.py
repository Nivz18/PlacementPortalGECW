# Generated by Django 5.0.2 on 2024-02-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='WYD', max_length=30),
        ),
    ]