# Generated by Django 4.2.6 on 2023-11-29 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ficheros', '0004_moto_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moto',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='auto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='autos_photos/'),
        ),
    ]