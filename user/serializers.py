from rest_framework import serializers
from .models import *


class RulesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'

class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
