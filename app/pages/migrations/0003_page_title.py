# Generated by Django 3.2.12 on 2022-03-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220330_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='untitled', max_length=255),
            preserve_default=False,
        ),
    ]
