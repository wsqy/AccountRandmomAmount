# Generated by Django 2.1.5 on 2020-08-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tran', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='order_no',
            field=models.CharField(blank=True, default='', help_text='订单号', max_length=30, null=True, verbose_name='订单号'),
        ),
    ]