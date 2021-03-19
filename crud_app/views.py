#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : views.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 19.03.2021
# Last Modified Date: 19.03.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>
from django.shortcuts import render
from django.http import HttpResponse
from crud_app.models import *

# Create your views here.
def index(request):
    data = Music.objects.all()
    # context = {
     #        'object_list': data,
      #      }
    # return HttpResponse('you are at index page')
    return render(request, 'crud_app/index.html', {'object_list' : data})

def add(request):
    # return HttpResponse('you are at add page')
    ava_artist = Musician.objects.all()
    return render(request, 'crud_app/add.html', {'artist': ava_artist})

def update(request):
    # return HttpResponse('you are at update page')
    return render(request, 'crud_app/update.html')

def delete(request):
    return HttpResponse('you are at delete page')

def about(request):
    return render(request, 'crud_app/about.html')
