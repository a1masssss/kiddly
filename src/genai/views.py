from django.shortcuts import render


def lessons(request):
    return render(request, 'lessons.html')