from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def index(request):
    
    return HttpResponse(f'New item created: {new_item.name} - {new_item.description} - {new_item.price}')
