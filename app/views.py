from django.shortcuts import render
from django.http import StreamingHttpResponse,HttpResponse
# Create your views here.
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
class UserViewset(ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
class ChannelViewset(ModelViewSet):
    queryset = Channels.objects.all()
    serializer_class = ChannelSerializer
class UserInfo(APIView):
    def post(self,request):
        data = request.data 
        data  =  data.dict()
        try:
            user = TelegramUser.objects.get(telegram_id=data['telegram_id'])
            print(user)
            serializer = TelegramUserSerializer(user,partial=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except TelegramUser.DoesNotExist:
            
            return Response({'status':'OK'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'status':'OK'},status=status.HTTP_404_NOT_FOUND)
class DeleteChannel(APIView):
    def post(self,request):
        data = request.data 
        data  =  data.dict()
        try:
            channel = Channels.objects.get(channel_id=data['channel_id'])
            channel.delete()
        except Channels.DoesNotExist:
            pass
        except:
            pass
        return Response({'status':'OK'})