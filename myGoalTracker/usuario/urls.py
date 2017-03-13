from django.conf.urls import url
from django.contrib.auth import views as auth_views

from usuario.views import pagina_de_inicio
from usuario.views import registrar_usuario
from usuario.views import login_usuario
from usuario.views import logout_usuario
from usuario.views import perfil_usuario
from usuario.views import modificar_perfil_usuario


urlpatterns = [
    url(r'^$', pagina_de_inicio, name='/'),
    url(r'^registrar/', registrar_usuario),
    url(r'^login/', login_usuario),
    url(r'^logout/', logout_usuario),
    url(r'^perfil/', modificar_perfil_usuario, name='perfil'),
    url(r'^perfil_usuario/$', perfil_usuario, name='perfil_usuario'),
]
