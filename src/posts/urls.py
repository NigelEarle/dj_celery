from django.conf.urls import url
from .views import (
  index,
  create,
  detail,
  update,
  delete,
)

urlpatterns = [
  url(r'^$', index),
  url(r'^create/$', create),
  url(r'^(?P<id>\d+)/$', detail),
  url(r'^(?P<id>\d+)/edit/$', update),
  url(r'^(?P<id>\d+)/delete/$', delete),
]