# Generated by Django 5.1.7 on 2025-03-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trade_code', models.CharField(max_length=50)),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('open_price', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.BigIntegerField()),
            ],
        ),
    ]
