from django.shortcuts import render
from django.utils import timezone
from .models import Webscrapy

# Create your views here.
def post_list(request):
    posts = Webscrapy.objects.all() 
    return render(request, 'noticias/post_list.html', {'posts': posts}) #consulta o banco