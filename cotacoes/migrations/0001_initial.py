# Generated by Django 4.1 on 2022-08-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=12)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('bought_price', models.FloatField()),
                ('price_alert', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=12)),
                ('price_alert', models.FloatField()),
            ],
        ),
    ]
