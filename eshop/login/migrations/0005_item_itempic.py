# Generated by Django 2.1 on 2018-08-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180828_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemPic',
            field=models.CharField(default='https://pbs.twimg.com/profile_images/507251035929190400/BDUL3Uzt_400x400.png', max_length=200),
        ),
    ]
