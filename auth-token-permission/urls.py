from django.conf.urls import url, include

from . import views

# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers


urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
]