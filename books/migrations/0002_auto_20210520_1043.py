# Generated by Django 3.2.3 on 2021-05-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='longDescription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='shortDescription',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbthumbnailUrl',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
