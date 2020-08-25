from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('rule/create/', RulesCreateView.as_view()),
    path('profile/create/', ProfileCreateView.as_view()),
    #path('client/create/', ClientCreateView.as_view())
]
