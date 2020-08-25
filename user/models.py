from django.db import models
from banks.models import *
from django.contrib.auth.models import User
# Create your models here.
from .centerbank import *

class Rules(models.Model):
    id = models.IntegerField(primary_key = True, unique=True)
    amountrur_gr = models.IntegerField(verbose_name="Верхний предел суммы в рублях")
    amountrur_le = models.IntegerField(verbose_name="Нижний предел суммы в рублях")
    amountusd_gr = models.IntegerField(verbose_name="Верхний предел суммы в долларах", blank=True)
    amountusd_le = models.IntegerField(verbose_name="Нижний предел суммы в долларах", blank=True)
    amounteur_gr = models.IntegerField(verbose_name="Верхний предел суммы в евро", blank=True)
    amounteur_le = models.IntegerField(verbose_name="Нижний предел суммы в евро", blank=True)
    date_amount = models.IntegerField(verbose_name="Количество часов для суммы")
    date_count = models.IntegerField(verbose_name="Количество часов для счетчика")
    count = models.IntegerField(verbose_name="Количество транзакций")
    eur = models.BooleanField(verbose_name="Евро")
    usd = models.BooleanField(verbose_name="Доллар")
    rur = models.BooleanField(verbose_name="Рубли")
    TYPE_CLIENT = (
        (1, "Брокер"),
        (2, "Кредитная карта"),
        (3, "Дебетовая карта"),
        (4, "Юридическое лицо"),
        (5, "Сберегательный счет"),
    )
    t_client = models.IntegerField(choices=TYPE_CLIENT, blank=True, default=1, unique=True)

    def __str__(self):
        return self.get_t_client_display()

    def save(self, *args, **kwargs):
        dol = float(rate2.replace(',','.'))
        ero = float(rate.replace(',','.'))
        if not self.amountusd_gr:
            self.amountusd_gr = self.amountrur_gr // dol
        if not self.amountusd_le:
            self.amountusd_le = self.amountrur_le // dol
        if not self.amounteur_gr:
            self.amounteur_gr = self.amountrur_gr // ero
        if not self.amounteur_le:
            self.amounteur_le = self.amountrur_le // ero
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    type_client = models.ManyToManyField(Rules, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
