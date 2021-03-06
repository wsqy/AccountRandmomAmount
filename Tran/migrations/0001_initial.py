# Generated by Django 2.1.5 on 2020-06-19 17:47

import Tran.models
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
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('name', models.CharField(blank=True, help_text='同一日有多个批次任务最好设置批次名称', max_length=40, null=True, verbose_name='批次名称')),
                ('amount_total_min', models.PositiveIntegerField(verbose_name='每日总金额下限')),
                ('amount_total_max', models.PositiveIntegerField(verbose_name='每日总金额上限')),
                ('batch_total', models.PositiveSmallIntegerField(default=30, verbose_name='批次数')),
                ('batch_num_min', models.PositiveSmallIntegerField(default=3, verbose_name='每批次交易笔数下限')),
                ('batch_num_max', models.PositiveSmallIntegerField(default=7, verbose_name='每批次交易笔数上限')),
                ('status', models.BooleanField(default=False, verbose_name='是否完成')),
                ('remark', models.CharField(blank=True, help_text='该备注信息会自动填充到每笔转账备注中', max_length=40, null=True, verbose_name='交易备注')),
                ('file_no', models.CharField(default=Tran.models.random_str, max_length=6, verbose_name='文件编号')),
                ('template', models.CharField(choices=[('1', '福建模板'), ('2', '江西模板')], default='1', max_length=2, verbose_name='文件模板')),
            ],
            options={
                'verbose_name': '每日任务',
                'verbose_name_plural': '每日任务',
            },
        ),
        migrations.CreateModel(
            name='TaskBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_total', models.PositiveIntegerField(verbose_name='批次总金额')),
                ('batch_total', models.PositiveSmallIntegerField(default=3, verbose_name='批次交易笔数')),
                ('num', models.PositiveSmallIntegerField(verbose_name='批次编号')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tran.Task', verbose_name='所属日任务')),
            ],
            options={
                'verbose_name': '任务批次',
                'verbose_name_plural': '任务批次',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='任务日期')),
                ('amount', models.IntegerField(verbose_name='交易金额')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Buyer', verbose_name='买方')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.Seller', verbose_name='卖方')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tran.Task', verbose_name='所属日任务')),
                ('task_batch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tran.TaskBatch', verbose_name='所属日批次')),
            ],
            options={
                'verbose_name': '交易明细',
                'verbose_name_plural': '交易明细',
            },
        ),
    ]
