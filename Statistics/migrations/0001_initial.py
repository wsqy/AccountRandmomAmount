# Generated by Django 2.1.5 on 2020-08-05 16:03

import Statistics.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayBuyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('amount_total', models.IntegerField(default=0, verbose_name='日总交易金额(万元)')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Buyer', verbose_name='买方')),
            ],
            options={
                'verbose_name': '买方日交易额总量',
                'verbose_name_plural': '买方日交易额总量',
            },
        ),
        migrations.CreateModel(
            name='DayCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('amount_total', models.IntegerField(default=0, verbose_name='日总交易金额(万元)')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Company', verbose_name='集团子公司')),
            ],
            options={
                'verbose_name': '集团子公司日交易额总量',
                'verbose_name_plural': '集团子公司日交易额总量',
            },
        ),
        migrations.CreateModel(
            name='DaySeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('amount_total', models.IntegerField(default=0, verbose_name='日总交易金额(万元)')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Seller', verbose_name='卖方')),
            ],
            options={
                'verbose_name': '卖方日交易额总量',
                'verbose_name_plural': '卖方日交易额总量',
            },
        ),
        migrations.CreateModel(
            name='DaySellerProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('price', models.PositiveIntegerField(blank=True, default=0, help_text='购买单价', null=True, verbose_name='购买单价')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, help_text='订货量', null=True, verbose_name='订货量')),
                ('choice_scale', models.PositiveIntegerField(blank=True, default=Statistics.models.DaySellerProducts.random_choice_scale, help_text='备货比例', null=True, verbose_name='备货比例')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Products', verbose_name='购买商品')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Seller', verbose_name='卖方')),
            ],
            options={
                'verbose_name': '卖方每日销售表',
                'verbose_name_plural': '卖方每日销售表',
            },
        ),
        migrations.CreateModel(
            name='MouthBuyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8, verbose_name='月份')),
                ('amount_total', models.IntegerField(default=0, verbose_name='月总交易金额(万元)')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Buyer', verbose_name='买方')),
            ],
            options={
                'verbose_name': '买方月交易额总量',
                'verbose_name_plural': '买方月交易额总量',
            },
        ),
        migrations.CreateModel(
            name='MouthCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8, verbose_name='月份')),
                ('amount_total', models.IntegerField(default=0, verbose_name='月总交易金额(万元)')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Company', verbose_name='集团子公司')),
            ],
            options={
                'verbose_name': '集团子公司月交易额总量',
                'verbose_name_plural': '集团子公司月交易额总量',
            },
        ),
        migrations.CreateModel(
            name='MouthSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8, verbose_name='月份')),
                ('amount_total', models.IntegerField(default=0, verbose_name='月总交易金额(万元)')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Seller', verbose_name='卖方')),
            ],
            options={
                'verbose_name': '卖方月交易额总量',
                'verbose_name_plural': '卖方月交易额总量',
            },
        ),
    ]
