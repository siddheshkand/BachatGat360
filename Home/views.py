from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home/index.html')


def text(request):
    return render(request, 'Home/demo.txt')


def json(request):
    return render(request, 'Home/demo.json')
