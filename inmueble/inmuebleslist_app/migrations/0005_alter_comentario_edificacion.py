# Generated by Django 4.2.3 on 2023-09-01 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0004_alter_edificacion_empresa_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='edificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='inmuebleslist_app.edificacion'),
        ),
    ]
