# Generated by Django 4.2.6 on 2023-10-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockMaster_app', '0018_productos_fecha_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='useredit',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
