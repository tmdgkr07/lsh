# Generated by Django 2.0.5 on 2018-06-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180531_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('temperature', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.CharField(default='', max_length=50),
        ),
    ]
