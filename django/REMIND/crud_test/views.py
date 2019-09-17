from django.shortcuts import render, redirect
from .models import Data_base

# Create your views here.
def home(request):
    data_base = Data_base.objects.all()
    context = {
        'datas': data_base,
    }
    return render(request, 'crud_test/index.html', context=context)

def create(request):
    data = request.GET.get('data')
    row = Data_base()
    row.data = data
    row.save()
    return redirect('crud_test:home')

def edit(request):

def update(request):

def add(request):
    return render(request, 'crud_test/add.html')