from django.shortcuts import render
from .game_logic import TicTacToe

game_instance = TicTacToe()

def index(request):
    context = {'board': game_instance.board}
    return render(request, 'game/index.html', context)

def make_move(request):
    row = int(request.POST.get('row'))
    col = int(request.POST.get('col'))
    message = game_instance.get_move(row, col)
    context = {
        'board': game_instance.board,
        'message': message
    }
    return render(request, 'game/index.html', context)
