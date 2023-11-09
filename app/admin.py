from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(TelegramUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id']
    list_per_page = 10
@admin.register(Channels)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name','channel_id','subscribers']
    list_per_page = 10