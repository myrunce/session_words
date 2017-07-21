# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):    
    return render(request, 'words/index.html')

def process(request):
    try:
        request.session['words']
    except:
        request.session['words'] = []
    print request.session['words']
    if request.method == 'POST':
        if request.POST.get('font') == 'yes':
            fontsize = "Big"
        else:
            fontsize = "Small"
        context = {
            'word': request.POST.get('word'),
            'color': request.POST.get('color'),
            'font': fontsize,
            "date": strftime("%B %d %Y", gmtime()),
            "time": strftime("%X %p", gmtime())
        }
        request.session['words'].insert(0,context)
        request.session.modified = True
        return redirect('/')    

def clear(request):
    request.session['words'] = []
    return redirect('/')