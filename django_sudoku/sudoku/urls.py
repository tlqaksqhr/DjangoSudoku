from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/sudoku/check', views.check name='sudoku_check'),
    path('/sudoku/make', views.make_sudoku, name='sudoku_make'),
]