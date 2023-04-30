from django.http import HttpResponse
from django.shortcuts import render


def privacy_page(request):
    return render(request, "Privacy/privacy.html")
