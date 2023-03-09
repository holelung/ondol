from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def IndexView(request):
    return render(request, 'ondol/index.html')
