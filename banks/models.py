from django.db import models
# Create your models here
from user.models import Rules
#from datetime import datetime, timedelta
from datetime import datetime
from datetime import timedelta
from user.centerbank import *

def proverka(amount, currency, date_pub, type_client, payerin):
    dol = float(rate2.replace(',','.'))
    ero = float(rate.replace(',','.'))
    cnt = 1
    zi = Rules.objects.get(t_client=type_client)
    kin = Transaction.objects.filter(payer__id=payerin.id)
    if (currency=="RUR"):
        summa = amount
        if (zi.amountrur_gr < amount) or (zi.amountrur_le > amount):
            return True
    if (currency=="EUR"):
        summa = int(amount * ero)
        if (zi.amounteur_gr < amount) or (zi.amounteur_le > amount):
            return True
        if (zi.eur == False):
            return True
    if (currency=="USD"):
        summa = int(amount * usd)
        if (zi.amountusd_gr < amount) or (zi.amountrur_le > amount):
            return True
        if (zi.usd == False):
            return True
    for t in kin:
        d1 = datetime.strptime(str(t.date_pub)[:-7:], "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(str(datetime.now())[:-7:], "%Y-%m-%d %H:%M:%S")
        d3 = d2 + timedelta(hours=-zi.date_amount)
        d4 = d2 + timedelta(hours=-zi.date_count)
        if d1 > d3:
            cnt += 1
        elif d1 > d4:
            if (currency=="USD"):
                summa += int(summa * usd)
            elif (currency=="EUR"):
                summa += int(summa * ero)
            else:
                summa += summa
        else:
            break
    if cnt >= zi.count or summa > zi.amountrur_gr:
        return True
    return False

class Client(models.Model):
    client = models.CharField(max_length=150, db_index=True)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=150, default='musa@musa.ru')
    TYPE_CLIENT = (
        (1, "Брокер"),
        (2, "Кредитная карта"),
        (3, "Дебетовая карта"),
        (4, "Юридическое лицо"),
        (5, "Сберегательный счет"),
    )
    t_client = models.IntegerField(choices=TYPE_CLIENT)

    def __str__(self):
        return (str(self.id) + " : " + self.client + " " + self.get_t_client_display())

class Transaction(models.Model):
    payer = models.ForeignKey(Client, on_delete = models.CASCADE)
    id_transaction = models.AutoField(primary_key=True, auto_created=True, unique=True)
    TYPE_TRANS = (
        (1, "Перевод физ. лицу"),
        (2, "Перевод перевод юр. лицу")
    )
    t_trans = models.IntegerField(choices=TYPE_TRANS, verbose_name="Тип транзакции")
    amount = models.IntegerField(db_index=True, verbose_name="Сумма перевода")
    currency = models.CharField(max_length=3, verbose_name="Валюта")
    payer_bank_name = models.CharField(max_length=100, verbose_name="Банк плательщика")
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name="Дата проведения транзакции")
    payee = models.CharField(max_length=150, verbose_name="Получатель")
    payee_bank_name = models.CharField(max_length=150, verbose_name="Банк получателя")
    alert = models.BooleanField(blank=True)

    def save(self, *args, **kwargs):
        if not self.alert:
            self.alert = proverka(self.amount, self.currency, self.date_pub, self.payer.t_client, self.payer)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']
