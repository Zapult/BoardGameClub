from django.shortcuts import render, redirect
from .models import BoardGame
from .forms import BoardgameForm

def index(request):
    return render(request, 'board_games/index.html')

def boardgames(request):
    boardgames = BoardGame.objects.order_by('name')
    context = {'boardgames': boardgames}
    return render(request, 'board_games/boardgames.html', context)

def boardgame(request, boardgame_id):
    boardgame = BoardGame.objects.get(id=boardgame_id)
    context = {'boardgame': boardgame}
    return render(request, 'board_games/boardgame.html', context)

def new_boardgame(request):
    if request.method != 'POST':
        form = BoardgameForm()
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:boardgames')

    context = {'form': form}
    return render(request, 'board_games/new_boardgame.html', context)
