# Generated by Django 2.1 on 2018-09-03 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0006_auto_20180828_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=1)),
                ('order1', models.CharField(max_length=1)),
                ('order2', models.CharField(max_length=1)),
                ('order3', models.CharField(max_length=1)),
                ('order4', models.CharField(max_length=1)),
                ('order5', models.CharField(max_length=1)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
