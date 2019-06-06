# Generated by Django 2.1.5 on 2019-04-28 04:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitulo', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('cuerpo', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('imagen', models.ImageField(upload_to='noticias', verbose_name='Imagen')),
                ('url_noticia', models.URLField(blank=True, null=True, verbose_name='Link de noticia')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de ult. actualizacion')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubes.Club', verbose_name='Codigo de club')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-created'],
            },
        ),
    ]
