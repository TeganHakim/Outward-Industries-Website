# Generated by Django 4.1.2 on 2023-04-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnpost',
            name='display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='learnpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='learn_posts'),
        ),
    ]
