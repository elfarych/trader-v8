# Generated by Django 4.1.1 on 2022-09-14 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
        ('orders', '0003_order_loss_percent_order_profit_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coins.coin'),
        ),
    ]