# Generated by Django 5.0.6 on 2024-06-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0005_paquetes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paquetes',
            old_name='Destinatario',
            new_name='Ciudad',
        ),
        migrations.RemoveField(
            model_name='paquetes',
            name='Fecha',
        ),
        migrations.AddField(
            model_name='paquetes',
            name='Precio',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
