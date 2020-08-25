from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('transaction/create/', TransactionCreateView.as_view()),
    path('client/create/', ClientCreateView.as_view())
]
