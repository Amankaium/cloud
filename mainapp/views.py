from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')


def contact_us(request):
    form = ContactForm()
    context = {}
    context['form'] = form
    return render(request, 'mainapp/contact_us.html', context)
