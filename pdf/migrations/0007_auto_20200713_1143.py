# Generated by Django 3.0.3 on 2020-07-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0006_auto_20200713_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomestatement',
            name='operations1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='operations2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='profit1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='profit2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='profitTax1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='profitTax2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='revenue1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='revenue2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='tax1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='tax2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='year1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='year2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]