#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : views.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 19.03.2021
# Last Modified Date: 20.03.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from crud_app.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    data = Music.objects.all()
    # context = {
     #        'object_list': data,
      #      }
    # return HttpResponse('you are at index page')
    return render(request, 'crud_app/index.html', {'object_list' : data})

def add(request):
    if request.method == 'POST':
        music_data = Musician()
        all_music_data = Music()
        music_data.musician_first_name = request.POST.get('m_fname') 
        music_data.musician_last_name = request.POST.get('m_lastname') 
        music_data.save()
        # retrieve id where fname = m_fname
        s_id = Musician(musician_first_name = request.POST.get('m_fname'))
        all_music_data.song_title = request.POST.get('s_title') 
        all_music_data.album_name = request.POST.get('s_album') 
        all_music_data.release_date = request.POST.get('s_date') 
        all_music_data.singer_name = music_data
        all_music_data.save()
        messages.success(request, 'Submmision added!')
        return HttpResponseRedirect('/')
        
    else:
        return render(request, 'crud_app/add.html') 

def update(request, ar_id):
    # return HttpResponse('you are at update page')
    return render(request, 'crud_app/update.html')

def delete(request, mid):
    Music.objects.filter(id=mid).delete()
    messages.success(request, 'Record deleted!')
    return HttpResponseRedirect('/')

def about(request):
    return render(request, 'crud_app/about.html')
