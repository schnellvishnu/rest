# Generated by Django 3.2.13 on 2022-09-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, max_length=50, null=True)),
                ('model_object_id', models.CharField(blank=True, max_length=20, null=True)),
                ('history_event', models.CharField(blank=True, max_length=100, null=True)),
                ('history_message', models.CharField(blank=True, max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('changed_by', models.IntegerField(blank=True, null=True)),
                ('changed_fields', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]