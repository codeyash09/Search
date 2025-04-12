from django import forms
from .models import SearchResult
from django.contrib.auth.models import User

class ResultForm(forms.ModelForm):
  class Meta:
    model = SearchResult
    fields = '__all__'


class RegisterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username','password')