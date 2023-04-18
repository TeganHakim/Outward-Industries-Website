# Generated by Django 4.1.2 on 2023-04-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0006_learnpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnpost',
            name='url',
            field=models.CharField(blank=True, choices=[('learn-web-design/', 'learn-web-design/'), ('learn-software/', 'learn-software/'), ('learn-business/', 'learn-business/')], max_length=100, null=True),
        ),
    ]