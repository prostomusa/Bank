# Generated by Django 2.2.2 on 2020-05-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200507_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(related_name='groups', to='user.Rules', verbose_name='Группа'),
        ),
    ]
