from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('interiores/', views.contato, name='interiores'),
    path('projetos/', views.news_details, name='projetos'),
    path('year/<int:year>', views.news_anual, name='year<int>'),
    path('registro/', views.registro, name='add'),
    path('add_user/', views.add_user, name='adduser'),
    path('add_newsletter/', views.add_newsletter, name='add_newsletter'),
    path('local/', views.localizacao_projetos, name='localizacao'),
]
