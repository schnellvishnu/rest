# Generated by Django 3.2.16 on 2022-10-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionreport',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
