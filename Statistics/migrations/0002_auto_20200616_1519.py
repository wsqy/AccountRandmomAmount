# Generated by Django 2.1 on 2020-06-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Statistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybuyer',
            name='amount_total',
            field=models.IntegerField(default=0, verbose_name='日总交易金额(万元)'),
        ),
        migrations.AlterField(
            model_name='dayseller',
            name='amount_total',
            field=models.IntegerField(default=0, verbose_name='日总交易金额(万元)'),
        ),
        migrations.AlterField(
            model_name='mouthbuyer',
            name='amount_total',
            field=models.IntegerField(default=0, verbose_name='月总交易金额(万元)'),
        ),
        migrations.AlterField(
            model_name='mouthseller',
            name='amount_total',
            field=models.IntegerField(default=0, verbose_name='月总交易金额(万元)'),
        ),
    ]
