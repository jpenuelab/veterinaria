# Generated by Django 3.1 on 2020-10-07 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_raza', models.CharField(max_length=255)),
                ('estado', models.IntegerField()),
                ('id_tipo', models.ForeignKey(db_column='id_tipo', on_delete=django.db.models.deletion.DO_NOTHING, to='tipo.tipomascota')),
            ],
            options={
                'db_table': 'raza',
            },
        ),
    ]