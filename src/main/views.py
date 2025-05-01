from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def cards(request):
    return render(request, 'main/cards.html')