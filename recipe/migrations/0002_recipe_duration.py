# Generated by Django 4.2.13 on 2024-06-07 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
