# Generated by Django 3.2.12 on 2022-03-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20220330_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpiece',
            name='counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]