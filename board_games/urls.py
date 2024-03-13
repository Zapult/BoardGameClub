from django.urls import path
from . import views

app_name = 'board_games'
urlpatterns = [
    path('', views.index, name='index'),
]