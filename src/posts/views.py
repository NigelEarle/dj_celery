from django.shortcuts import render, redirect
from django.core import serializers

from .forms import CreateForm
from .models import Post
from .tasks import feedback_email_task

# Create your views here.

def index(request):
  return render(request, "index.html")

def detail(request, id=None):
  return render(request, "detail.html")

def create(request):
  form = CreateForm(request.POST)
  if form.is_valid():
    title = form.cleaned_data["title"]
    content = form.cleaned_data["content"]

    instance = form.save(commit=False)
    instance.user = request.user
    instance.save()
    job = feedback_email_task.delay(title, "nigel@earle.io", content)
  context = {
    "form": form,
  }

  return render(request, "create.html", context)

def update(request, id=None):
  return render(request, "update.html")

def delete(request, id=None):
  return redirect("posts:index")