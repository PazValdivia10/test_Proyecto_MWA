# Generated by Django 2.2 on 2019-04-29 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='club_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clubes.Club', verbose_name='Codigo de club'),
        ),
    ]
