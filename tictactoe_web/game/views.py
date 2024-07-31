from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .game_logic import TicTacToe
import json

game_instance = TicTacToe()

def index(request):
    context = {'board': game_instance.board, 'message': ''}
    return render(request, 'game/index.html', context)

@csrf_exempt
def make_move(request):
    data = json.loads(request.body)
    row = data['row']
    col = data['col']
    message = game_instance.get_move(row, col)
    board_html = render_to_string('game/board.html', {'board': game_instance.board})
    return JsonResponse({'board_html': board_html, 'message': message})
