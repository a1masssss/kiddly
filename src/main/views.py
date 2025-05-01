from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import View

from main.utils.generators.openai_gen import generate_stream_response


def home(request):
    return render(request, 'main/home.html')

def cards(request):
    return render(request, 'main/cards.html')

def playground(request):
    return render(request, 'main/playground.html')

class OpenAIView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/playground.html')
        
    def post(self, request, *args, **kwargs):
        return StreamingHttpResponse(generate_stream_response(request), content_type='text/event-stream')
