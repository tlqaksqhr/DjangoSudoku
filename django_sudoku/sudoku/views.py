from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates
from .api.sudoku import Sudoku

# Create your views here.

def index(request):
    return HttpResponse("Index Page!")

def check_sudoku(request):
    return HttpResponse("Check Page!")

def make_sudoku(request):

    sudoku_api = Sudoku()
    board = sudoku_api.generate_puzzle()
    result = {
        'board' : board
    }

    return JsonResponse(result)