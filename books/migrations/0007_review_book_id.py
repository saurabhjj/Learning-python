# Generated by Django 3.2.3 on 2021-05-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=1),
        ),
    ]
