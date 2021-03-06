# Generated by Django 2.2.2 on 2020-05-09 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20200509_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type_client',
            field=models.ManyToManyField(blank=True, to='user.Rules'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
