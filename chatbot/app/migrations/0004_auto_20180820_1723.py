# Generated by Django 2.0.5 on 2018-08-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180607_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='place',
            field=models.FloatField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='weather',
            name='status',
            field=models.FloatField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.FloatField(default='', max_length=50),
        ),
    ]
