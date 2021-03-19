#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : models.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 19.03.2021
# Last Modified Date: 19.03.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>
from django.db import models

# Create your models here.
class Musician(models.Model):
    musician_first_name = models.CharField(max_length=30)
    musician_last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.musician_first_name

class Music(models.Model):
    song_title = models.CharField(max_length=30)
    album_name = models.CharField(max_length=30)
    release_date = models.DateField()
    singer_name = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title






