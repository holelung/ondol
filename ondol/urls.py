from django.urls import path
from django.urls import path

from . import views

app_name = 'ondol'
urlpatterns = [
    path('', views.IndexView),
]
