# Generated by Django 4.1 on 2022-11-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
