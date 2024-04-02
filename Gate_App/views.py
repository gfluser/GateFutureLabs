from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "html")


def about(request):
    return render(request, 'about.html')


def terms(request):
    return render(request, 'terms.html')


def privacy(request):
    return render(request, 'privacy.html')


def contact(request):
    return render(request, 'contact.html')


def subscribe(request):
    return render(request, 'subscribe.html')


def blog(request):
    return render(request, 'grid.html')


def details(request):
    return render(request, 'details.html')


def join(request):
    return render(request, 'join.html')


def summary(request):
    return render(request, 'summary.html')

