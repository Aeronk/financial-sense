# Generated by Django 3.0.3 on 2020-07-05 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file',
            field=models.FileField(default='null', upload_to='docs'),
        ),
    ]