# Generated by Django 4.2.11 on 2024-05-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_completedorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeorders',
            name='final_address_coordinates',
            field=models.TextField(default='', verbose_name='Координати кінцевої адреси'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activeorders',
            name='starting_address_coordinates',
            field=models.TextField(default='', verbose_name='Координати початкової адреси'),
            preserve_default=False,
        ),
    ]
