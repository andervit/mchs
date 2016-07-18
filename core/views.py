# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.db.models import F
import math
from django.http import JsonResponse



def home(request):
    data = Substance.objects.all()[:10]
    return render(request, 'core/index.html', {'size':len(data),'data':data})

def test(request):
    text = request.GET.get('name')
    pros = int(request.GET.get('pros'))
    vol = int(request.GET.get('vol'))
    dist = int(request.GET.get('dist'))


    pros = pros/100.0
    substance = Substance.objects.get(name=text)

    mass = substance.density * vol * pros
    diameter = 5.33*(mass**0.327)
    heigth = diameter/2
    Fq = (heigth/diameter + 0.5)/(4*(((heigth/diameter + 0.5)**2 + (dist/diameter)**2))**1.5)
    teta = math.exp(-0.0007*((dist**2 + diameter**2)**0.5 - diameter))

    q = 450*Fq*teta
    time = 0.92*(mass**0.303)

    data = {'q':q, 'time':time}

    return JsonResponse(data)
