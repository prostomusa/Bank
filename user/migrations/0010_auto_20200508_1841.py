# Generated by Django 2.2.2 on 2020-05-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200508_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='group', to='user.Rules', verbose_name='Группа'),
        ),
    ]
