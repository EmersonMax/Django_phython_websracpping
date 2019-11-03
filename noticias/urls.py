from django.urls import path
from . import views
#pagina criada para o projeto
urlpatterns = [
    path('', views.post_list, name='post_list'),
]