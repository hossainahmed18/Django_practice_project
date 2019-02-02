from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class registrationForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = [

            'first_name',
            'last_name',
            'username',

            'email',
            'password1',
            'password2',

        ]
