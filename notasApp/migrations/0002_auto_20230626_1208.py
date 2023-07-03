# Generated by Django 3.2.12 on 2023-06-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaNotasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterModelOptions(
            name='notasmodel',
            options={'verbose_name': 'notas'},
        ),
        migrations.AddField(
            model_name='notasmodel',
            name='categorias',
            field=models.ManyToManyField(to='notasApp.CategoriaNotasModel'),
        ),
    ]
