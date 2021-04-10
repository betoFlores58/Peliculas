from django.urls import path
from .views import HomeListView, peliculaView, peliculaCreateView,peliculaUpdateView,peliculaDeleteView, CatalogoTemplateView, registro,catalogo,contacto, UserChangePasswordView
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('<int:pk>/ver', peliculaView.as_view(), name='pelicula_view'),
    path('', HomeListView.as_view(), name='home'),
    #path('catalogo', CatalogoTemplateView.as_view(), name='catalogo'),
    path('catalogo/',catalogo,name='catalogo'),
    path('contacto/',contacto,name='contacto'),
    path('peli/Nueva', peliculaCreateView.as_view(), name='nuevaPelicula'),
    path('peli/<int:pk>/editar', peliculaUpdateView.as_view(), name='editarPelicula'),
    path('delete/<int:pk>/', peliculaDeleteView.as_view(), name = 'eliminarPelicula'),
    path('registro/',registro,name="registro"),
    #path('changePassword/',UserChangePasswordView.as_view(),name='user_change_password'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html',success_url = '/'),name='change_password'),
]