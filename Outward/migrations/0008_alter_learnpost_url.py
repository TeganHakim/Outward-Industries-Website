# Generated by Django 4.1.2 on 2023-04-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0007_learnpost_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnpost',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]