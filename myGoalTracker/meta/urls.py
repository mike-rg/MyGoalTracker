from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^principal/', views.principal, name='principal'),
]
