# Generated by Django 4.1.1 on 2022-09-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('stop_loss', models.FloatField(blank=True, null=True)),
                ('take_profit', models.FloatField(blank=True, null=True)),
                ('reason_density', models.CharField(blank=True, max_length=30, null=True)),
                ('reason_price', models.CharField(blank=True, max_length=30, null=True)),
                ('loss_order', models.BooleanField(default=False)),
                ('profit_order', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
