from django.urls import path
from main.views import home, cards

urlpatterns = [
    path('', home, name = 'home'),
    path('cards/', cards, name = 'cards')
]

