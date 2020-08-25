"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from banks import views
import user
from .views import redirect_blog
urlpatterns = [
    path('', redirect_blog),
    #path('/login', user.views.login_page, name='login_url'),
    path('admin/', admin.site.urls),
    path('api/v1/bank/', include('banks.urls')),
    path('api/v1/user/', include('user.urls')),
    path('blog/<int:id_transaction>/', views.transaction_detail, name='tran_detail'),
    path('blog/<int:id>', views.id_transactions, name='id_transaction'),
    path('blog', views.transactions, name='our_blog'),
    path('alert', views.alert_list, name='alert_list'),
    path('export', views.export, name='export_url'),
    path('export2', views.export2, name='export2_url'),
    path('users/<str:username>/', user.views.UserDetailMixin.as_view(), name='user_detail'),
    path('users/<str:username>/update', user.views.UserUpdateMixin.as_view(), name='user_update'),
    path('users/<str:username>/gr_update', user.views.UserProfileUpdateMixin.as_view(), name='user_update_group'),
    path('users/<str:username>/delete', user.views.UserDeleteMixin.as_view(), name='user_delete'),
    path('user/create', user.views.UserCreateMixin.as_view(), name='user_create'),
    path('users', user.views.user_list, name='user_list'),
    path('rules/<int:t_client>/update', user.views.RulesUpdateMixin.as_view(), name='rule_update'),
    path('rules', user.views.rules_list, name='rules_list'),
    path('login', user.views.login_page, name='login_url'),
    path('logout/', user.views.logoutUser, name="logout"),
    path('mypage/', user.views.page, name="mypage"),
]
