# Generated by Django 3.2.12 on 2023-06-26 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notasApp', '0002_auto_20230626_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='notasmodel',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]