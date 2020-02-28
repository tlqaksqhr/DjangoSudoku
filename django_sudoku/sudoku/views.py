from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates

# Create your views here.

def index(request):
    return HttpResponse("Index Page!")

def check(request):
    return HttpResponse("Check Page!")

def make_sudoku(request):
    return HttpResponse("Sudoku Make Page!")