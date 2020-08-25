# Generated by Django 2.2.2 on 2020-05-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200506_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rules',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='rules',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='rules',
            name='user',
        ),
        migrations.AddField(
            model_name='rules',
            name='amountrur',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='eur',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='rur',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='usd',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(to='user.Rules'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='t_client',
            field=models.IntegerField(blank=True, choices=[(1, 'Брокер'), (2, 'Кредитная карта'), (3, 'Дебетовая карта'), (4, 'Юридическое лицо'), (5, 'Сберегательный счет')], default=1, unique=True),
        ),
    ]
