# Generated by Django 2.1.5 on 2019-06-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20190428_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='cuerpo',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]
