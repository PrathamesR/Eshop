# Generated by Django 2.1 on 2018-09-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20180903_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv',
            name='order1',
            field=models.CharField(blank=True, default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='inv',
            name='order2',
            field=models.CharField(blank=True, default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='inv',
            name='order3',
            field=models.CharField(blank=True, default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='inv',
            name='order4',
            field=models.CharField(blank=True, default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='inv',
            name='order5',
            field=models.CharField(blank=True, default=None, max_length=1),
        ),
    ]
