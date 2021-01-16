from django.http  import HttpResponse,Http404
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')