# Generated by Django 3.2.6 on 2021-09-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210908_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='catid',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='userid',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='userid',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]