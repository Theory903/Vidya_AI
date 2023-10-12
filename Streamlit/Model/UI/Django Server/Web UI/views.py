from django.shortcuts import render

# WEBUI/views.py
from django.shortcuts import render
from .models import ChatMessage
from .forms import ChatForm

def chat_view(request):
    messages = ChatMessage.objects.all()
    form = ChatForm()
    return render(request, 'HTML/chat.html', {'messages': messages, 'form': form})
