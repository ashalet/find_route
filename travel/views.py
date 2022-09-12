from django.shortcuts import render


def home(request):
    empty = "empty"
    return render(request, 'home.html', {'empty': empty})
