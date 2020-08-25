# Generated by Django 2.2.2 on 2020-05-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='allow',
        ),
        migrations.RemoveField(
            model_name='user',
            name='t_client',
        ),
        migrations.AddField(
            model_name='rules',
            name='t_client',
            field=models.IntegerField(blank=True, choices=[(1, 'Брокер'), (2, 'Кредитная карта'), (3, 'Дебетовая карта'), (4, 'Юридическое лицо'), (5, 'Сберегательный счет')], default=1),
        ),
    ]
