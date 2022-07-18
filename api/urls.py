from django.urls import path
from . import views
from django.contrib import admin
# from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('', views.inicio, name='inicio'),
                  path('users', views.users, name='users'),
                  path('users/crear', views.crearusers, name='crearusers'),
                  path('users/editar', views.editarusers, name='editarusers'),
                  path('excercises', views.excercises, name='excercises'),
                  path('excercises/crear', views.crearexcercises, name='crearexcercises'),
                  path('excercises/editar', views.editarexcercises, name='editarexcercises'),
                  path('excercises/eliminar', views.eliminarexcercises, name='eliminarexcercises'),
                  path('routines', views.routines, name='routines'),
                  path('routines/crear', views.crearroutines, name='crearroutines'),
                  path('routines/editar', views.editarroutines, name='editarroutines'),
                  path('admin/', admin.site.urls),
                  path('showlist/', views.showlist, name='showlist'),
                  # path('excercise/eliminar/<int:id>', views.eliminar, name='eliminar'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
