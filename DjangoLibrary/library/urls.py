from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('add/', add, name='add'),
    path('addbook/', addbook, name='addbook'),
]