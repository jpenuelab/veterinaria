# Generated by Django 3.1 on 2020-10-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='motivo',
            field=models.TextField(default='N/A', max_length=2000),
            preserve_default=False,
        ),
    ]