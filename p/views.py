from django.shortcuts import render
from django.http import JsonResponse, Http404

from .models import *
from .forms import *


def index(request):
    context = {}
    if request.method == 'GET':
        context['form'] = LandingForm()
    if request.method == 'POST':
        form = LandingForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context['form'] = LandingForm()
            context['modal'] = 'thank you'
        else:
            context['modal'] = 'landing'
    return render(request, 'index.html', context)


def mapdisplay(request):
    context = {}
    context['center'] = Area.objects.get(name='UQ').address.position
    context['carparks'] = Carpark.objects.filter(verified=True)

    return render(request, 'map.html', context)
