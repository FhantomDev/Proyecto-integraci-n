# Generated by Django 4.2.6 on 2024-06-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferremax', '0003_pedido_direccionpedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='idOrden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='idSesion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
