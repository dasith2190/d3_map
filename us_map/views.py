from django.shortcuts import render
from django.http import *
from django.shortcuts import reverse, render
# Create your views here.

def test_map(request):
    return render(request, 'test_map.html',)