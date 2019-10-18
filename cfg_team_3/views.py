from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse('Hello')

def index(request):
    return render(request, 'cfg_team_3/index.html')


# def processed(request):
#     return HttpResponse('We are at processed function we created')

