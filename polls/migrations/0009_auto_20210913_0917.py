# Generated by Django 3.2.6 on 2021-09-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='catid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='userid',
            field=models.IntegerField(null=True),
        ),
    ]