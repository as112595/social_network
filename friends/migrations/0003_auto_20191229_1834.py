# Generated by Django 3.0.1 on 2019-12-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20191229_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='connected_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
