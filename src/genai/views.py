from django.shortcuts import render


def genai(request):
    return render(request, 'genai.html')