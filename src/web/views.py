from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from web.models import Accordation, Annoucement, Category, Company, EventNews, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, News, PhotoEvent, Post, Postsection, Product, Slide, Smallcard, Timeline
from .forms import ContactForm

# Create your views here.

def index(request):

    slide = Slide.objects.get(positionhero=1)
    smallcard = Smallcard.objects.filter(positionhero=2)
    company = Company.objects.get(id=1)
    hero1 = Herotypeone.objects.get(positionhero=3)
    hero4 = Herotypetwo.objects.get(positionhero=4)
    hero3 = Herotypethree.objects.get(positionhero=6)
    hero5 = Herotypefour.objects.get(positionhero=7)
    hero7 = Heroseven.objects.get(positionhero=2)
    accordation = Accordation.objects.filter(positionhero=5).order_by('sortnumber').filter(status=True)
    context = {

        'slide':slide,
        'com':company,
        'smcard':smallcard,
        'hero1':hero1,
        'hero4':hero4,
        'hero3':hero3,
        'hero5':hero5,
        'hero7':hero7,
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

def semiconductor(request):
    return render(request, 'pages/semiconductor.html')
def pv(request):
    return render(request, 'pages/pv.html')

def contactus(request):

    form = ContactForm(request.POST or None)
    if request.method == 'POST':

        contactname = request.POST['contactname']
        companyname = request.POST['companyname']
        contactmail = request.POST['contactemail']
        subjects = request.POST['enquirysubject']
       
        if form.is_valid():
            form.save()
            form = ContactForm

            subject = 'Welcome to TT Vision Holding Berhad'
            subject2 = f'{contactname}, From {companyname}, - {subjects},'
            message = f'Hi {contactname}, thank you for contact us .'
            message2 = f'Hi {contactname}, thank you for contact us .'
            email_from = settings.SERVER_EMAIL
            recipient_list = [contactmail, ]
            recipient_list2 = ['adrewlee@ttvision-tech.com','sales@ttvision-tech.com'],['syed.afiq@ttvision-tech.com']

        
            send_mail(subject, message, email_from, recipient_list,fail_silently=False,)

            return redirect('')
        else:
            print(form.errors)
            print('fail to save')
    

    
    context = {
        'form':form
    }
    return render(request, 'pages/contact.html',context)

def award(request):
    
    company = Company.objects.get(id=1)
    post = Post.objects.get(slug="awardandachievment")
    timeline = Timeline.objects.all().order_by('position')
    context = {
        'com':company,
        'timeline':timeline,
        'about':'Award and Achievement',
        'post':post
    }

    return render(request, 'pages/award.html',context)

def event(request,slug):

    events = EventNews.objects.filter(slug=slug).first()
    eventtitle = EventNews.objects.all()
    pe = PhotoEvent.objects.filter(postlib__slug=slug)
    context = {
        'etitle':eventtitle,
        'e':events,
        'pe':pe,

    }
    return render(request, 'pages/event.html',context)

def news(request):
    nw = News.objects.all()
    context = {
        'news':nw,
    }
    return render(request, 'pages/news.html',context)

def newslist(request):
    nw = News.objects.all()
    context = {
        'news':nw,
    }
    return render(request, 'pages/blog-list.html',context)

def press(request):
    nw = News.objects.all()
    context = {
        'news':nw,
    }
    return render(request, 'pages/press.html',context)

def newsm(request):
    return render(request, 'pages/media.html')

def robotic(request):
    return render(request, 'pages/robotic.html')

def pvinspect(request):
    return render(request, 'pages/inspectionlist.html')

def semiconductorlist(request):
    return render(request, 'pages/semiconductorlist.html')

def rpv(request, slug):

    pr = Product.objects.get(productslug=slug)

    context = {
        'pr':pr
    }
    return render(request, 'pages/productviews.html',context)

def pinspection(request, slug):

    pr = Product.objects.get(productslug=slug)

    context = {
        'pr':pr
    }
    return render(request, 'pages/productviews.html',context)

def icled(request, slug):
    pr = Product.objects.get(productslug=slug)
    context = {
        'pr':pr
    }

    return render(request, 'pages/productviews.html',context)


def semi1(request):
    return render(request, 'pages/semiconductor.html')
def semi2(request):
    return render(request, 'pages/semiconductor2.html')
def semi3(request):
    return render(request, 'pages/semiconductor3.html')

def investor(request):

    iv = Annoucement.objects.all()
    b = Category.objects.filter(catype=1)

    context = {
        'title':'Investor Relation - Announcement',
        'iv':iv,
        'bursa':b,
    }
    return render(request, 'pages/invester.html',context)

def career(request):

    context = {
        'title':'Careers'
    }
    return render(request, 'pages/career.html')




    
