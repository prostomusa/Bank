# Generated by Django 2.2.2 on 2020-05-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20200509_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='amounteur_gr',
            field=models.IntegerField(blank=True, default=100, verbose_name='Верхний предел суммы в евро'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='amounteur_le',
            field=models.IntegerField(blank=True, default=10, verbose_name='Нижний предел суммы в евро'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='amountusd_gr',
            field=models.IntegerField(blank=True, default=100, verbose_name='Верхний предел суммы в долларах'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='amountusd_le',
            field=models.IntegerField(blank=True, default=10, verbose_name='Нижний предел суммы в долларах'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='date_amount',
            field=models.IntegerField(default=1, verbose_name='Количество часов для суммы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rules',
            name='count',
            field=models.IntegerField(verbose_name='Количество транзакций'),
        ),
        migrations.AlterField(
            model_name='rules',
            name='date_count',
            field=models.IntegerField(verbose_name='Количество часов для счетчика'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type_client',
            field=models.ManyToManyField(blank=True, to='user.Rules'),
        ),
    ]
