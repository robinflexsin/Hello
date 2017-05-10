from django.conf.urls import url, include
from .views import MyView

urlpatterns = [
    url(r'^my/$', MyView, name='my'),
]