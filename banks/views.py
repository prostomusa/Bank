from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from django.core.paginator import Paginator
from user.models import UserProfile
from .filters import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from user.models import *
from django.db.models import Q
from djpjax import pjax

tira = Transaction.objects.all()
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionDetailSerializer

class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientDetailSerializer

@login_required
def transactions(request):
    posts = Transaction.objects.all()
    myFilter = OrderFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    return render(request, 'bank/reg.html', {'posts': posts, 'myFilter': myFilter})

@login_required
def id_transactions(request, id):
    posts = Transaction.objects.filter(payer_id=id)
    tren = posts[0].payer.client
    return render(request, 'bank/client_transactions.html', context={'posts': posts, 'tren': tren})

@login_required
def alert_list(request):
    user = UserProfile.objects.get(user__username=request.user)
    posts = Transaction.objects.filter(Q(alert=True) & Q(payer__t_client__in=user.type_client.all()))
    return render(request, 'bank/alerts_list.html', {'posts': posts})

@login_required
def transaction_detail(request, id_transaction):
    post = Transaction.objects.get(id_transaction=id_transaction)
    return render(request, 'bank/trans_detail.html', {'post': post})

@login_required
def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['ID', 'Тип транзакции', 'сумма', 'валюта', 'банк плательщика', 'дата транзакции', 'Банк получателя', 'Alert'])
    for member in Transaction.objects.all().values_list('id_transaction', 't_trans', 'amount', 'currency', 'payer_bank_name', 'date_pub', 'payee', 'payee_bank_name', 'alert'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="transaction.csv"'

    return response

@login_required
def export2(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    user = UserProfile.objects.get(user__username=request.user)
    writer.writerow(['ID', 'Тип транзакции', 'сумма', 'валюта', 'банк плательщика', 'дата транзакции', 'Банк получателя', 'Alert'])
    for member in Transaction.objects.filter(Q(alert=True) & Q(payer__t_client__in=user.type_client.all())).values_list('id_transaction', 't_trans', \
    'amount', 'currency', 'payer_bank_name', 'date_pub', 'payee', 'payee_bank_name', 'alert'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="alert.csv"'

    return response
