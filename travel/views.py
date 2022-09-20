from django.shortcuts import render


def home(request):
    empty = "home"
    return render(request, 'home.html', {'empty': empty})


def about(request):
    empty = "about"
    return render(request, 'about.html', {'empty': empty})
