from django.db import models
from django.utils.html import format_html 
# Create your models here.
class TelegramUser(models.Model):
    name = models.CharField(null=True,blank=True,verbose_name="Full name",max_length=150)
    telegram_id = models.CharField(max_length=150,unique=True,verbose_name="Telegram ID")
    def __str__(self):
        if self.name:
            return self.name
        else:
            return f"USER: {self.telegram_id}"
    class Meta:
        verbose_name = "Bot User "
        verbose_name_plural = "Bot Users "

class Channels(models.Model):
    channel_id = models.CharField(max_length=5000,null=True,blank=True,unique=True)
    name = models.CharField(max_length=5000,null=True,blank=True)
    subscribers = models.CharField(max_length=5000,null=True,blank=True)
    def __str__(self):
        return 'Channel ID'
    class Meta:
        verbose_name = 'CHANNEL ID'
        verbose_name_plural = 'CHANNELS ID'
    