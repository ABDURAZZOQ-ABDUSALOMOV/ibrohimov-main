from django.shortcuts import render
from .api_views import *

def homepage(request):
    context = {
        'viloyatlar' : Viloyat.objects.all(),
        'tumanlar' : Tuman.objects.all(),
    }
    return render(request, 'index.html', context)

        