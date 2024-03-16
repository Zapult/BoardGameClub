from django.urls import path
from . import views

app_name = 'board_games'
urlpatterns = [
    path('', views.index, name='index'),
    path('boardgames/', views.boardgames, name='boardgames'),
    path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('new_boardgame/', views.new_boardgame, name='new_boardgame'),
    path('new_loan/', views.new_loan, name='new_loan'),
]
