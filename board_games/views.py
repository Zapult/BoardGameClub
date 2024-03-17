from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BoardGame, Loan
from .forms import BoardgameForm, LoanForm

def index(request):
    return render(request, 'board_games/index.html')

@login_required
def boardgames(request):
    boardgames = BoardGame.objects.order_by('name').all()
    context = {'boardgames': boardgames}
    return render(request, 'board_games/boardgames.html', context)

@login_required
def boardgame(request, boardgame_id):
    boardgame = BoardGame.objects.get(id=boardgame_id)
    context = {'boardgame': boardgame}
    return render(request, 'board_games/boardgame.html', context)

@login_required
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

@login_required
def new_loan(request):
    boardgames = BoardGame.objects.all()
    context = {'boardgames': boardgames}

    user = request.user
    user_loan_count = Loan.objects.filter(user=user).count()
    
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            game_id = form.cleaned_data['game']
            game = BoardGame.objects.get(id=game_id)
            
            if user_loan_count >= 3:
                messages.error(request, "You have already borrowed three games!")
            else:
                if game.loaned:
                    messages.error(request, f"The game {game.name} is already loaned!")
                else:
                    loan = Loan(user=user, game=game)
                    loan.save()
                    game.loaned = True
                    game.save()
                    messages.success(request, f"You have succesfully borrowed {game.name}. Your current loans: {user_loan_count} games loaned.")
                    return redirect('board_games:index')

    else:
        form = LoanForm()
    return render(request, 'board_games/new_loan.html', {'form': form, 'boardgames': boardgames})

@login_required
def loaned_games(request):
    loaned_games = Loan.objects.filter(user=request.user)
    return render(request, 'board_games/loaned_games.html', {'loaned_games': loaned_games})
