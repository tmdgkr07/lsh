# Generated by Django 2.0.5 on 2018-05-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(default='', max_length=30)),
                ('menu', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
