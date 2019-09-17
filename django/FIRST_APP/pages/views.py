from django.shortcuts import render
from django.http import HttpResponse
# from lotto import lotto_num
from random import sample, randint

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    name = '오재석'
    data = ['강동주', '김지수', '정의진']
    context = {
        'name': name,
        'data': data,
        'movie': ['aaa','bbbbb','cccccccccc'],
        'lotto_num': [1, 12, 43],
        'number': 10
    }

    return render(request, 'home.html', context)

def lotto(request):
    # num = lotto_num()
    num = sample(range(1,46),6)
    context = {
        'lotto_num': num,
        'movie': ['aaa','bbbbb','cccccccccc'],
    }
    return render(request, 'lotto.html', context)

def cube(request, num):
    context = {
        'result': num**3,
    }
    return render(request, 'cube.html', context)

def match(request):
    context = {
        'me': request.POST.get('me'),
        'you': request.POST.get('you'),
        'result': randint(50,100),
    }

    return render(request, 'match.html', context)