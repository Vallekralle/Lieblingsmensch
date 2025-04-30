from django.views.generic import TemplateView, CreateView
from django.shortcuts import render

from .models import *


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class MessageCreateView(CreateView):
    template_name = "pages/create_message.html"
    model = Message
    fields = ["receiver", "content"]


def search_message(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        messages = Message.objects.filter(receiver__contains=searched).order_by('-created_at')
        return render(
            request, 
            "pages/search_message.html", 
            {
            "searched": searched,
            "messages": messages,
            }
        )
    else:
        return render(
            request,
            "pages/search_message.html",
            {},
        )
