# Generated by Django 3.2.12 on 2023-09-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('D', 'Borrador'), ('P', 'Publicado')], max_length=1)),
            ],
        ),
    ]
