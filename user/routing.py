from django.urls import path
from .consumers import ChatConsumer
from .consumers2 import WSConsumer2
ws_urlpatterns =[
    path('ws/url/',ChatConsumer.as_asgi()),
    path('ws/url2/',WSConsumer2.as_asgi())
]