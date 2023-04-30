# Generated by Django 4.1.6 on 2023-04-22 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("MessageID", models.AutoField(primary_key=True, serialize=False)),
                ("SendDateTime", models.DateTimeField(auto_now_add=True)),
                ("UpdateDateTime", models.DateTimeField(auto_now=True)),
                ("Text", models.TextField()),
                ("Viewed", models.BooleanField(default=False)),
                (
                    "Recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Recipient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "Sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
