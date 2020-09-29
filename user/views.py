from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework import generics
from .serializers import *
from .forms import *
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import redirect
from .centerbank import *
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages, admin
from import_export.admin import ImportExportModelAdmin
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


euro1 = euro()
dollar1 = dollar()

class RulesCreateView(generics.CreateAPIView):
    serializer_class = RulesDetailSerializer

class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileDetailSerializer

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userm = authenticate(request, username=username, password=password)

        if userm is not None:
            login(request, userm)
            return redirect('our_blog')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'bank/login.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    return render(request, 'bank/user_list.html', context={'users': users})

@login_required
def rules_list(request):
    users = UserProfile.objects.get(user__username=request.user)
    return render(request, 'bank/rules_list.html', context={'users': users})

@login_required
def logoutUser(request):
	logout(request)
	return redirect('login_url')

@login_required
def page(request):
    users = get_object_or_404(User, username__iexact=str(request.user))
    us = UserProfile.objects.filter(user=users.id)
    if len(us) < 1:
        return render(request, 'bank/mypage.html', context={'users': users, 'us': us})
    else:
        return render(request, 'bank/mypage.html', context={'users': users, 'us': us[0]})


class UserDetailMixin(LoginRequiredMixin, View):

    def get(self, request, username):
        users = get_object_or_404(User, username__iexact=username)
        us = UserProfile.objects.filter(user=users.id)
        if len(us) < 1:
            return render(request, 'bank/user_detail.html', context={'users': users, 'us': us})
        else:
            return render(request, 'bank/user_detail.html', context={'users': users, 'us': us[0]})


class UserCreateMixin(LoginRequiredMixin, View):

    def get(self, request):
        form = UserForm()
        return render(request, 'bank/user_create.html', context={'form': form, 'detail': True})

    def post(aelf, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('user_list')
        return render(request, 'bank/user_create.html', context={'form': form, 'detail': True})


class UserUpdateMixin(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = User
    model_form = UserForm
    template = 'bank/user_update.html'


class UserProfileUpdateMixin(LoginRequiredMixin, GroupObjectUpdateMixin, View):
    model1 = User
    model2 = UserProfile
    model_form = UserProfileForm
    template = 'bank/group_update.html'

class RulesUpdateMixin(LoginRequiredMixin, View):

    def get(self, request, t_client):
        rule = Rules.objects.get(t_client=t_client)
        bound_form = RulesForm(instance=rule)
        return render(request, 'bank/rule_update.html', context={'form': bound_form, 'rule': rule})

    def post(self, request, t_client):
        rule = Rules.objects.get(t_client=t_client)
        bound_form = RulesForm(request.POST, instance=rule)
        if bound_form.is_valid():
            new_rule = bound_form.save()
            return redirect('rules_list')
        return render(request, 'bank/rule_update.html', context={'form': bound_form, 'rule': rule})


class UserDeleteMixin(LoginRequiredMixin, View):

    def get(self, request, username):
        user = User.objects.get(username__iexact=username)
        return render(request, 'bank/user_delete.html', context={'user': user})

    def post(self, request, username):
        user = User.objects.get(username__iexact=username)
        user.delete()
        return redirect(reverse('user_list'))
