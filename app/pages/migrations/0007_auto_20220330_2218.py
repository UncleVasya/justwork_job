# Generated by Django 3.2.12 on 2022-03-30 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('pages', '0006_alter_contentpiece_counter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentpiece',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='contentpiece',
            unique_together={('title', 'polymorphic_ctype_id')},
        ),
    ]