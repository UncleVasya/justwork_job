# Generated by Django 3.2.12 on 2022-03-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pieceonpage',
            options={'ordering': ['piece_order']},
        ),
        migrations.AddField(
            model_name='pieceonpage',
            name='piece_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
