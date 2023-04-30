from django.db import models
from django.contrib.auth.models import User
from Accounts.models import CustomUser


class Message(models.Model):
    MessageID = models.AutoField(primary_key=True, blank=False)
    Sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Sender')
    Recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Recipient')
    SendDateTime = models.DateTimeField(auto_now_add=True)
    UpdateDateTime = models.DateTimeField(auto_now=True)
    Text = models.TextField(blank=False)
    Viewed = models.BooleanField(default=False)
