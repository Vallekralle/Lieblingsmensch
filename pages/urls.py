from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("create/", MessageCreateView.as_view(), name="create"),
    path("search/", search_message, name="search"),
]