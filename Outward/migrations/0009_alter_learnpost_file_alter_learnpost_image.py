# Generated by Django 4.1.2 on 2023-04-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0008_alter_learnpost_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='learnpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
