from django.shortcuts import render
from datetime import datetime


def index(request):
    current_year = datetime.now().year
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def menu(request):
    return render(request, 'restaurant/menu.html')

def menu_item(request, id):
    return render(request, 'restaurant/menu_item.html', {'id': id})

def book(request):
    return render(request, 'restaurant/book.html')

def bookings(request):
    return render(request, 'restaurant/bookings.html')

def login(request):
    return render(request, 'restaurant/login.html')
