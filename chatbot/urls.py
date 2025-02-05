from django.urls import path
from .views import chat_with_gpt, chatbot_ui

urlpatterns = [
    path('', chatbot_ui, name='chatbot_ui'),
    path('api/chat/', chat_with_gpt, name='chat_with_gpt'),
]