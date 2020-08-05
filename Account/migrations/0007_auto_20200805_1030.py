# Generated by Django 2.1.5 on 2020-08-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_corporation_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corporation',
            options={'verbose_name': '交易场所', 'verbose_name_plural': '交易场所'},
        ),
        migrations.AddField(
            model_name='corporation',
            name='is_activate',
            field=models.BooleanField(blank=True, default=True, help_text='该交易场所是否继续使用', null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='businessscope',
            name='is_activate',
            field=models.BooleanField(blank=True, default=True, help_text='该分类是否继续使用', null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_activate',
            field=models.BooleanField(blank=True, default=True, help_text='该公司是否继续使用', null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='corporation',
            name='name',
            field=models.CharField(help_text='交易场所', max_length=40, verbose_name='交易场所'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_activate',
            field=models.BooleanField(blank=True, default=True, help_text='该商品是否继续使用', null=True, verbose_name='状态'),
        ),
    ]
