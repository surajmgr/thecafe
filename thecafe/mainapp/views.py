from django.shortcuts import render
from .models import carousel, Information

# Create your views here.


def carousels(request):

    acarousel = carousel.objects
    ainfo = Information.objects

    return render(request, 'mainapp/index.html', {'acarousel': acarousel, 'ainfo': ainfo})


def error_404(request, exception=None):
    return render(request, 'mainapp/error_404.html')
