from .models import *
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, username):
        users = self.model.objects.get(username__iexact=username)
        bound_form = self.model_form(instance=users)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): users})

    def post(self, request, username):
        users = self.model.objects.get(username__iexact=username)
        bound_form = self.model_form(request.POST, instance=users)

        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect('user_list')
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): users})

class GroupObjectUpdateMixin:
    model1 = None
    model2 = None
    model_form = None
    template = None

    def get(self, request, username):
        users = self.model1.objects.get(username__iexact=username)
        users_pr = self.model2.objects.filter(user=users.id)
        if len(users_pr) < 1:
            tin = self.model2(user=users)
            tin.save()
            bound_form = self.model_form(instance=tin)
        else:
            bound_form = self.model_form(instance=users_pr.first())
        return render(request, self.template, context={'form': bound_form, self.model2.__name__.lower(): users_pr.first()})

    def post(self, request, username):
        users = self.model1.objects.get(username__iexact=username)
        users_pr = self.model2.objects.filter(user=users.id)
        bound_form = self.model_form(request.POST, instance=users_pr.first())

        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect('user_list')
        return render(request, self.template, context={'form': bound_form, self.model2.__name__.lower(): users_pr.first()})
