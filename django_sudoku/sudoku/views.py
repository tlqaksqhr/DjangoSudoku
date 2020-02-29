from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates
from sudoku.models import Ranking
from .api.sudokus import Sudoku

from .models import Ranking

import json
import datetime

# Create your views here.

def index(request):
    context = {}
    return render(request, 'sudoku/index.html',context)

def get_ranking_list():
    ranking_list = Question.objects.order_by('-pub_date')[:100]
    return JsonResponse(ranking_list)

def register_ranking(request):

    if 'elapsed_time' not in request.session:
        return JsonResponse({'status' : 'failed'})

    name = request.POST['name']
    elapsed_time = request.session['elapsed_time']

    ## TODO : save ranking info to database

    datetime_args = elapsed_time/3600,(elapsed_time%3600)/60,elapsed_time%60
    d = datetime.time(datetime_args[0], datetime_args[1], datetime_args[2]) 

    ranking = Ranking(name = name, elapsed_time = d)
    ranking.save()

    return JsonResponse({'status' : 'success'})

def check_sudoku(request):
    sudoku_api = Sudoku()

    req_data = json.loads(request.body)

    puzzle = req_data['puzzle']
    elapsed_time = req_data['elapsed_time']

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