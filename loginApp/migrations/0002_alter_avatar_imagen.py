# Generated by Django 3.2.12 on 2023-01-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatares'),
        ),
    ]
