from django.http import HttpResponse
from django.shortcuts import render


def password_reset_page(request):
    return render(request, "PasswordReset/password_reset.html")
