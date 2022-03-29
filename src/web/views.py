from django.shortcuts import render

from web.models import Accordation, Company, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, Post, Postsection, Slide, Smallcard

# Create your views here.

def index(request):

    slide = Slide.objects.get(positionhero=1)
    smallcard = Smallcard.objects.filter(positionhero=2)
    company = Company.objects.get(id=1)
    hero1 = Herotypeone.objects.get(positionhero=3)
    hero4 = Herotypetwo.objects.get(positionhero=4)
    hero3 = Herotypethree.objects.get(positionhero=6)
    hero5 = Herotypefour.objects.get(positionhero=7)
    accordation = Accordation.objects.filter(positionhero=5).order_by('sortnumber')
    context = {

        'slide':slide,
        'com':company,
        'smcard':smallcard,
        'hero1':hero1,
        'hero4':hero4,
        'hero3':hero3,
        'hero5':hero5,
        'accordation':accordation
    }
    return render(request,'pages/frontpage.html',context)

def companybackground(request):
    company = Company.objects.get(id=1)
    post = Post.objects.get(slug="historyandbussiness")
    context = {
        'com':company,
        'about':'Company Background',
        'post':post
    }
    return render(request, 'pages/companybackground.html',context)

def vision(request):
    postvision = Postsection.objects.get(id=1)
    hero5 = Herotypefive.objects.get(positionhero=1)
    hero7 = Heroseven.objects.get(positionhero=2)
    company = Company.objects.get(id=1)
    context = {
        'com':company,
        'pv':postvision,
        'hero5':hero5,
        'hero7':hero7,
        
    }

    return render(request, 'pages/vision.html',context)

    
