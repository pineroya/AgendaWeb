# Generated by Django 3.2.12 on 2023-06-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('camponota', models.TextField(max_length=600)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
