from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<h1>Trick tool here</h1>')
