# Generated by Django 3.0.3 on 2020-07-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0014_auto_20200726_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomestatement',
            name='add_value1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='add_value2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='add_value3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='incomestatement',
            name='add_value4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
