# Generated by Django 5.0.2 on 2024-02-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=50)),
                ('ctc', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
