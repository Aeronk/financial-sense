# Generated by Django 3.0.3 on 2020-07-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0012_addfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomestatement',
            name='earnings1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='incomestatement',
            name='earnings2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='incomestatement',
            name='expenses1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='incomestatement',
            name='expenses2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
