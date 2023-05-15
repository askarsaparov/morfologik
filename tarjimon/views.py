from django.shortcuts import render
from django.http import HttpResponse

from .forms import DictioForm
from .logic import read_file
from .models import Lugat

def index(request):
    soz = request.GET.get('q', '')
    if soz and soz != '':
        result = read_file(soz)
        # print(result)
    else:
        result = None
        soz = None
    return render(request, 'index.html', {'q': soz, 'natija': result, 'soz': soz})

def salom2(request):
    return render(request, '')