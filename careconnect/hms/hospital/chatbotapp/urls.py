from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_messages, name='list_messages'),
    path('send/', views.send_message, name='send_message'),
    path('clear/', views.clear_chat, name='clear_chat'),
]