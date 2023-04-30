from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


def login_page(request):
    if request.user.is_authenticated:
        return redirect('messenger')
    if request.method == 'POST':
        # print(request.POST)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f'You are now logged in as {username}.')
                return redirect('messenger')
        messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='Login/login.html', context={'form': form})
