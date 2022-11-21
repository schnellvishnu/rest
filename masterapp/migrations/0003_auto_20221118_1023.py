# Generated by Django 3.2.5 on 2022-11-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0002_alter_locations_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='ShipToLocationLookupid',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='locations',
            name='address',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='locations',
            name='city',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='locations',
            name='country',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='locations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='created_by',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='locations',
            name='state',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='locations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='zip',
            field=models.CharField(default=True, max_length=20),
        ),
    ]