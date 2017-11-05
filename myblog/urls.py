from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.blogDetail, name="entry_detail")
]
