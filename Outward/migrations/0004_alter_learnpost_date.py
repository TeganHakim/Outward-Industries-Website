# Generated by Django 4.1.2 on 2023-04-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0003_learnpost_type_alter_learnpost_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnpost',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
