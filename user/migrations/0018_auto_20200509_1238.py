# Generated by Django 2.2.2 on 2020-05-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20200509_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='type_client',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type_client',
            field=models.ManyToManyField(to='user.Rules'),
        ),
    ]