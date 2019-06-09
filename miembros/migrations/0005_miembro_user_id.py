# Generated by Django 2.1.5 on 2019-06-07 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miembros', '0004_auto_20190529_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='user_id',
            field=models.OneToOneField(default=99, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
