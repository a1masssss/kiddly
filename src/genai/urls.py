from django.urls import path
from genai.views import lessons


urlpatterns = [
    path('', lessons, name = 'lessons')
]