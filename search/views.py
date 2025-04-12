from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import SearchResult
from .forms import ResultForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.
class search(ListView):
  template_name = 'search.html'

  def get_queryset(self):
    return SearchResult.objects.all()


def result_new(request):
  if(request.method == "POST"):
    form = ResultForm(request.POST)
    if(form.is_valid()):
      post = form.save(commit=False)
      post.save()
      return redirect('search')
  else:
    form = ResultForm()
  return render(request, 'result_edit.html', {'form': form})


def signup_new(request):
  if(request.method == "POST"):
    form =  RegisterForm(request.POST)
    if(form.is_valid()):
      
      
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      post = form.save(commit=False)
      post.save()
      user = User.objects.get(username = username)
      user.set_password(password)
      user.save()
        
        
      
      


      return redirect('login')
  else:
    form = RegisterForm()
  return render(request, 'registration/signup.html', {'form': form})