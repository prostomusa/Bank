# Generated by Django 2.2.2 on 2020-05-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0003_remove_client_id_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='t_client',
        ),
        migrations.AddField(
            model_name='client',
            name='t_client',
            field=models.IntegerField(choices=[(1, 'Брокер'), (2, 'Кредитная карта'), (3, 'Дебетовая карта'), (4, 'Юридическое лицо'), (5, 'Сберегательный счет')], default=1),
            preserve_default=False,
        ),
    ]