from django.shortcuts import render
from .models import Home, About, Skill, Service, Portfoilo, Blog

# Create your views here.


def home (request):
    home = Home.objects.last()
    about = About.objects.last()
    skill = Skill.objects.all()
    service = Service.objects.all()
    portfolio = Portfoilo.objects.all()
    text_portofolio = Portfoilo.objects.last()
    blog = Blog.objects.all()






    return render (request,'home.html', {
        'home':home,
        'about':about,
        'skill':skill,
        'service':service,
        'portfolio':portfolio,
        'text_portofolio':text_portofolio,
        'blog':blog,

                                         
                                         
                                         
                                         
        })