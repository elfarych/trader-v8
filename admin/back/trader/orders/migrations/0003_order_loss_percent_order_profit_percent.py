# Generated by Django 4.1.1 on 2022-09-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_price_alter_order_stop_loss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='loss_percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='profit_percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
