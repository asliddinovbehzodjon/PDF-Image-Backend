from rest_framework import serializers
from .models import *
class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = '__all__'

