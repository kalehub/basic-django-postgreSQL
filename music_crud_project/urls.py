#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : urls.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 19.03.2021
# Last Modified Date: 19.03.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'music_crud_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url('',include('crud_app.urls')),
        
]
