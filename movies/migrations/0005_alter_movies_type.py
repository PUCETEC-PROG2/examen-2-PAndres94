# Generated by Django 4.2 on 2024-07-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movies_sinopsis_alter_movies_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='type',
            field=models.CharField(choices=[('R', 'Romance'), ('T', 'Terror'), ('A', 'Accion'), ('M', 'Miedo'), ('C', 'Comedia')], max_length=30),
        ),
    ]
