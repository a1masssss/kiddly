from django.urls import path
from main.views import home, cards, OpenAIView

urlpatterns = [
    path('', home, name = 'home'),
    path('cards/', cards, name = 'cards'),
    path('playground/', OpenAIView.as_view(), name = 'playground')
]



