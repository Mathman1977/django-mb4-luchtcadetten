# Generated by Django 3.2.6 on 2021-08-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mb4', '0002_auto_20210815_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='opgave',
            name='moeilkhgr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]