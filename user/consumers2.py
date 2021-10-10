from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async
import asyncio
import json
import random
from django.contrib.auth.models import User
import time


class WSConsumer2(WebsocketConsumer):

    def connect(self):
        self.accept()
        all_users=User.objects.all()
        liste=[]
        for i in all_users:
            liste.append(i.username)
        self.send(json.dumps({'user':liste}))
