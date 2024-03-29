# Generated by Django 4.1.2 on 2023-04-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Outward', '0002_learnpost_display_learnpost_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnpost',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'Web Design'), ('2', 'Software'), ('3', 'Business')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='learnpost',
            name='author',
            field=models.CharField(blank=True, choices=[('1', 'Tegan Hakim'), ('2', 'Tyler Lumpkin'), ('3', 'Outward Industries')], max_length=100, null=True),
        ),
    ]
