# Generated by Django 4.2.15 on 2024-12-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_portfolio_education_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='work_experience',
            field=models.TextField(blank=True, null=True),
        ),
    ]
