from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('the server has started')

