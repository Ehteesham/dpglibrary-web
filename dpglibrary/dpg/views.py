from django.shortcuts import render
from .models import ml_list
from math import ceil
# Create your views here.
def index(request):
    return render(request, 'dpg/index.html')

def contact(request):
    return render(request, 'dpg/contact.html')

def ml_page(request):
    ml = ml_list.objects.all()
    params = {'ml':ml, 'n':len(ml)}
    return render(request, 'dpg/ml_page.html', params)