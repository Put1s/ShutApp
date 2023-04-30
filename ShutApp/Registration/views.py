from django.shortcuts import render, redirect
from Accounts.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def registration_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, 'Registration successful.')
            return redirect('messenger')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = CustomUserCreationForm()
    return render(request=request, template_name='Registration/registration.html', context={'register_form': form})