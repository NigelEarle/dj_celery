from django.shortcuts import render, redirect
from .forms import CreateForm
from .models import Post


# Create your views here.

def index(request):
  return render(request, "index.html")

def detail(request, id=None):
  return render(request, "detail.html")

def create(request):
  form = CreateForm(request.POST)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.user = request.user
    instance.save()
    
  context = {
    "form": form,
  }

  return render(request, "create.html", context)

def update(request, id=None):
  return render(request, "update.html")

def delete(request, id=None):
  return redirect("posts:index")