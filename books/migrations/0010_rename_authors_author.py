# Generated by Django 3.2.3 on 2021-05-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210524_1035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]