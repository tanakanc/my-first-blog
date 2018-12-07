# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:12:59 2018

@author: tanakanc
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]