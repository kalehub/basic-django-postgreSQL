#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : urls.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 19.03.2021
# Last Modified Date: 20.03.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>


from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('add/', views.add, name='add'),
        path('update/', views.update, name='update'),
        path('del/<int:mid>', views.delete, name='delete'),
        path('about/<int:ar_id>', views.about, name='about'),
]



