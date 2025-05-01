from django.urls import path
from genai.views import genai


urlpatterns = [
    path('', genai, name = 'genai')
]