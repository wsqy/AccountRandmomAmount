# Generated by Django 2.1.5 on 2020-08-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='total_range',
            field=models.CharField(choices=[('1', '200万以内'), ('2', '200万-500万'), ('3', '超过500万'), ('12', '500万以内'), ('23', '200万以上'), ('123', '不限金额')], help_text='单笔定金范围', max_length=1, verbose_name='单笔定金范围'),
        ),
        migrations.AlterField(
            model_name='products',
            name='total_range',
            field=models.CharField(choices=[('1', '200万以内'), ('2', '200万-500万'), ('3', '超过500万'), ('12', '500万以内'), ('23', '200万以上'), ('123', '不限金额')], help_text='单笔定金范围', max_length=3, verbose_name='单笔定金范围'),
        ),
    ]
