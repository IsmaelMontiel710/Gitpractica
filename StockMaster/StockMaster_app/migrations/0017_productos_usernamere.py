# Generated by Django 4.2.6 on 2023-10-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0016_alter_productos_hora_baja'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='usernamere',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
