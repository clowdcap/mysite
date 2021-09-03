from django.contrib import admin
from django.urls import path, include
# from News.views import home, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('News.urls')),
    #path('', home, name='home'),
    #path('contato/', contato, name='contato'),
]

