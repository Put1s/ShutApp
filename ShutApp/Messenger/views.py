from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from Accounts.models import CustomUser
from Accounts.managers import CustomUserManager
from Accounts.functions import get_fields
from .models import Message
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import datetime


def messenger_page(request):
    # obj = CustomUser.objects.get(username=request.user.username)
    # obj.birth_date = datetime.date(day=23, month=3, year=2006)
    # obj.save()
    return render(request, 'Messenger/messenger.html', context={"users_number": len(CustomUser.objects.all())})


def messenger_logout(request):
    logout(request)
    return redirect('messenger')


def user_page(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        return render(request, 'Messenger/user.html', context=get_fields(CustomUser, user))
    except Exception as e:
        # print(e)
        return render(request, 'Messenger/user_does_not_exist.html')


@csrf_exempt
def dm_page(request, username):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        user = CustomUser.objects.get(username=username)
        # self_id = CustomUser.objects.get(username=request.user.username).id
        # user_id = CustomUser.objects.get(username=username).id
        # if self_id == user_id:
        #     messages = Message.objects.filter(Sender_id=self_id, Recipient_id=user_id).order_by('SendDateTime')
        # else:
        #     messages = messages = Message.objects.filter(
        #         Q(Sender_id=self_id, Recipient_id=user_id) |
        #         Q(Sender_id=user_id, Recipient_id=self_id)).order_by('SendDateTime')
        if request.user == user:
            messages = Message.objects.filter(Sender=request.user, Recipient=user).order_by(
                'SendDateTime')
        else:
            messages = Message.objects.filter(
                Q(Sender=request.user, Recipient=user) |
                Q(Sender=user, Recipient=request.user)).order_by('SendDateTime')
        # print(self_id, user_id)
        if request.method == 'POST':
            print(request.POST.get('typed_message'))
            Message.objects.create(Text=request.POST.get('typed_message'), Sender=request.user,
                                   Recipient=user).save()
            return redirect(f'/messenger/dm/{username}')
        return render(request, 'Messenger/dm.html', context={'username': username, 'messages': messages})
    except Exception as e:
        print(e)
        return render(request, 'Messenger/user_does_not_exist.html')


def people_page(request):
    return render(request, 'Messenger/people.html', context={'users': CustomUser.objects.all()})
