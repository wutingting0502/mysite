from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def hello(request):
    context = {}
    context['helloWorld'] = 'Hello World!'
    return render(request, 'helloWorld.html', context)