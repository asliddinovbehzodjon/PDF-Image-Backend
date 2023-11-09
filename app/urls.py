from .views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('channel',ChannelViewset)
router.register('user',UserViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('userinfo/',UserInfo.as_view()),
    path('delete/',DeleteChannel.as_view())
]
