from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username')  # Update the import statement

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class LinkedInBio(models.Model):
    title = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
