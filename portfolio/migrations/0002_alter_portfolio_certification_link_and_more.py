# Generated by Django 4.2.16 on 2024-09-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='certification_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='project_link',
            field=models.CharField(max_length=255),
        ),
    ]
