# Generated by Django 4.2.11 on 2024-04-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_time', models.DateTimeField(verbose_name='Час відкриття замовлення')),
                ('starting_address', models.TextField(verbose_name='Початкова адреса')),
                ('final_address', models.TextField(verbose_name='Кінцева адреса')),
            ],
            options={
                'verbose_name': 'Активне замовлення',
                'verbose_name_plural': 'Активні замовлення',
            },
        ),
    ]
