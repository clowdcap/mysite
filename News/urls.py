from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('details/', views.news_details, name='details'),
    path('year/<int:year>', views.news_anual, name='year<int>'),
    path('registro/', views.registro, name='add'),
    path('add_user/', views.add_user, name='adduser'),
    path('add_newsletter/', views.add_newsletter, name='add_newsletter'),
]
