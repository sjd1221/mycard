# Generated by Django 3.2.6 on 2021-09-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_userdet_userphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='userid',
            field=models.IntegerField(null=True),
        ),
    ]