# Generated by Django 3.2.3 on 2021-05-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210520_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='shortDescription',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
