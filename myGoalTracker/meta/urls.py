from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^principal/', views.principal, name='principal'),
    url(r'^crea_meta/', views.crear_meta, name='crear_meta'),
    url(r'^listar_metas/', views.listar_metas, name='listar_metas')
]
