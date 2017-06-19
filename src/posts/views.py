from django.shortcuts import render, redirect

# Create your views here.

def index(request):
  return render(request, "index.html")

def detail(request, id=None):
  return render(request, "detail.html")

def create(request, id=None):
  return render(request, "create.html")

def update(request, id=None):
  return render(request, "update.html")

def delete(request, id=None):
  return redirect("posts:index")