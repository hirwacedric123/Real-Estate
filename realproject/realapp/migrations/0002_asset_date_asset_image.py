# Generated by Django 4.1.7 on 2023-04-12 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='asset',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
