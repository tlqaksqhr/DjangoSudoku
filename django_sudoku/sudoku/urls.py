from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sudoku/check', views.check_sudoku, name='check_sudoku'),
    path('sudoku/make', views.make_sudoku, name='make_sudoku'),
]