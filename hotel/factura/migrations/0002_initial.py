# Generated by Django 5.0.6 on 2024-06-25 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factura', '0001_initial'),
        ('reservar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='codigo_R',
            field=models.ForeignKey(db_column='codigo_R', on_delete=django.db.models.deletion.CASCADE, to='reservar.reserva'),
        ),
        migrations.AddField(
            model_name='factura',
            name='codigo_FP',
            field=models.ForeignKey(db_column='Codigo_FP', on_delete=django.db.models.deletion.CASCADE, to='factura.forma_p'),
        ),
    ]
