# Generated by Django 3.2.4 on 2021-07-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20210708_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]