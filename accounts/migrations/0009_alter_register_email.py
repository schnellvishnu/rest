# Generated by Django 3.2.16 on 2022-10-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20221017_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
