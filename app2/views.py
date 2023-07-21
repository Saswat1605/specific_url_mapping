from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>I AM python developer<h1>')
def second(request):
    return HttpResponse('<h1>i am Django developer<h1>')

