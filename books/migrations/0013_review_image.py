# Generated by Django 3.2.3 on 2021-05-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images/review'),
        ),
    ]
