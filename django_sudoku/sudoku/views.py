from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates
from .api.sudoku import Sudoku

# Create your views here.

def index(request):
    context = {}
    return render(request, 'sudoku/index.html',context)

def register_ranking(request):
    pass

def check_sudoku(request):
    sudoku_api = Sudoku()
    puzzle = request.POST['puzzle']
    elapsed_time = request.POST['time']

    result = sudoku_api.sudoku_check(puzzle)
    data = {}
    if result == True:
        data['status'] = "clear"
        request.session['status'] = "clear"
        request.session['elapsed_time'] = elapsed_time
    else:
        data['status'] = "fail"

    return JsonResponse(data)

def make_sudoku(request):

    sudoku_api = Sudoku()
    board = sudoku_api.generate_sudoku()
    result = {
        'board' : board
    }

    return JsonResponse(result)