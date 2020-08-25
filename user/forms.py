from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError

class RulesForm(forms.ModelForm):

    class Meta:
        model = Rules
        fields = ['amountrur_gr','amountrur_le','amountusd_gr','amountusd_le','amounteur_gr', \
                  'amounteur_le','date_amount','date_count','count','eur','usd']
                  
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['type_client']
        widgets = {
            'type_client': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
