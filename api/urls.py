from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('', views.inicio, name='inicio'),
                  path('user', views.user, name='user'),
                  path('user/crear', views.crearuser, name='crearuser'),
                  path('user/editar', views.editaruser, name='editaruser'),
                  path('excersice', views.excersice, name='excersice'),
                  path('excersice/crear', views.crearexcersice, name='crearexcersice'),
                  path('excersice/editar', views.editarexcersice, name='editarexcersice'),
                  path('routine', views.routine, name='routine'),
                  path('routine/crear', views.crearroutine, name='crearroutine'),
                  path('routine/editar', views.editarroutine, name='editarroutine'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
