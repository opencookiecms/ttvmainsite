from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseServerError,HttpResponseRedirect
from web.models import Accordation, Annoucement, Category, Company, EventNews, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, News, PhotoEvent, Post, Postsection, Product, Productfeas, Slide, Smallcard, Timeline,AnnoucementMeetings, Newsletter,Pressrelease, Metapro
from .forms import ContactForm, NewsletterForm, HrForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json, requests, os


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
    meta = Metapro.objects.get(position=1)
  
    context = {

        'slide':slide,
        'com':company,
        'smcard':smallcard,
        'hero1':hero1,
        'hero4':hero4,
        'hero3':hero3,
        'hero5':hero5,
        'hero7':hero7,
        'accordation':accordation,
        'meta':meta
   
    }
   
    return render(request,'pages/frontpage.html',context)
    

def companybackground(request):
    company = Company.objects.get(id=1)
    post = Post.objects.get(slug="historyandbussiness")
    meta = Metapro.objects.get(position=2)
    context = {
        'title': 'Company Background',
        'com':company,
        'about':'Company Background',
        'post':post,
        'meta':meta,
        'keywords': "technology, technology company, technology driven, automated machine vision, pc-based vision systems, vision systems, TTVHB, TT Vision Holdings Berhad, TTVTSB, TT Vision Technologies Sdn Bhd, TTICSB, TT Innovation Centre Sdn Bhd, investment holding company, development and manufacturing, development, manufacturing, manufacturing and development, vision inspection module, optoelectronics, solar wafer, solar cell, discrete components, IC chips, vision guided robotic equipment, vision guided robot, semiconductor components, Goon Koon Yin, Wong Yih Hsow, Jennie Tan Yen-Li",
        'description': "TT Vision's Company Background"
    }
    return render(request, 'pages/companybackground.html',context)

def vision(request):
    postvision = Postsection.objects.get(id=1)
    hero5 = Herotypefive.objects.get(positionhero=1)
    hero7 = Heroseven.objects.get(positionhero=2)
    company = Company.objects.get(id=1)
    context = {
        'title': 'Vision and Mission',
        'com':company,
        'pv':postvision,
        'hero5':hero5,
        'hero7':hero7,
        'keywords': "mission, vision, mission and vision, vision and mission, innovate, equipment inspection, innovate equipment inspection, leading brand, equipment vision inspection, vision inspection",
        'description': "TT Vision's Mission and Vision"
    }

    

    return render(request, 'pages/vision.html',context)

def semiconductor(request):
    return render(request, 'pages/semiconductor.html')
def pv(request):
    return render(request, 'pages/pv.html')

def contactus(request):
    company = Company.objects.get(id=1)
    meta = Metapro.objects.get(position=3)
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # contactname = request.POST['contactname']
        # companyname = request.POST['companyname']
        # contactmail = request.POST['contactemail']
        # subjects = request.POST['enquirysubject']
        # country = request.POST['country']
        # how = request.POST['looking']
        # tel = request.POST['contacttel']
        # content = request.POST['enquirycontent']
       
        if form.is_valid():
            form.save()
            #subject = 'Welcome to TT Vision Holding Berhad'
            #message2 = render_to_string('pages/mail2.html',{
                #'name':contactname,
                #'company':companyname,
                #'mail':contactmail,
                #'con':country,
                #'how':how,
                #'tel':tel,
                #'mailtext':content,
                #'sub':subjects
            #})
            #text2content = strip_tags(message2)

            #message = render_to_string('pages/mail.html',{'pr':contactname})
            #textcontent = strip_tags(message)
            
            #email_from = settings.SERVER_EMAIL
            #recipient_list = [contactmail, ]
            #recipient_list2 = ['syed.afiq@ttvision-tech.com']

            #subject1, from_email, to = subjects, email_from, recipient_list
            #subject2, from2_email,to2 = subjects, email_from,recipient_list2

            #msg = EmailMultiAlternatives(subject1,textcontent,from_email,to)
            #msg.attach_alternative(message, "text/html")
            #msg.send()

            #msg2 = EmailMultiAlternatives(subject2,text2content,from2_email,to2)
            #msg2.attach_alternative(message2,"text/html")
            #msg2.send()
        

        
            #send_mail(subject, message, email_from, recipient_list,fail_silently=False,)

            #email contents
            subject = 'Enquiries regarding ' + form.cleaned_data["enquirysubject"]
            message = f'Name: {form.cleaned_data["contactname"]}\nCompany Name: {form.cleaned_data["companyname"]}\nEmail: {form.cleaned_data["contactemail"]}\nPhone Number: {form.cleaned_data["contacttel"]}\nCountry: {form.cleaned_data["country"]}\nHow did they find out about us: {form.cleaned_data["looking"]}\nEnquiry Subject:\n {form.cleaned_data["enquirysubject"]}\nEnquiry Message:\n {form.cleaned_data["enquirycontent"]}'
            #domain email
            from_email = settings.SERVER_EMAIL
            #recipient email
            recipient_list = ['mvr-enews@ttvision-tech.com']
            #attaching contents to the email to be sent
            email = EmailMessage(subject, message, from_email, recipient_list)
            email.send()
            #redirect to success
            return redirect('contactdone')
        else:
            print(form.errors)
            print('Failed to send')
    
    context = {
        'title': 'Job Application',
        'form':form,
        'com':company,
        'meta':meta,
        'keywords': "contact, contact us, location, tel, telephone, email, fax, phone, hr@ttvision-tech.com, 604-6456294, 604-6456295, job, job application, career",
        'description': "Apply for a job in TT Vision. Contact Us At Email: 'hr@ttvision-tech.com' | Tel: 604-6456294 | Fax:604-6456295 | Location: Plot 106, Hilir Sungai Keluang 5, Bayan Lepas Phase 4, 11900, Penang, Malaysia"
    }
    return render(request, 'pages/contact.html',context)

def newsletter(request):
    form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = NewsletterForm
            return redirect('contactdone')
        else:
            print(form.errors)
            print("error")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    
# if noindex=true, robot meta tag is set to noindex and nofollow    
def contactdone(request):
    company = Company.objects.get(id=1)
    context = {
        'title': 'Contact Us',
        'com':company,
        'noindex': True,
    }
    return render(request, 'pages/success.html',context)

def award(request):
    
    company = Company.objects.get(id=1)
    post = Post.objects.get(slug="awardandachievment")
    timeline = Timeline.objects.all().order_by('position')
  
    context = {
        'title': 'Awards and Achievements',
        'com':company,
        'timeline':timeline,
        'about':'Awards and Achievements',
        'post':post,
        'keywords': "1-inno cert, 1-inno cert rating AAA, SME, SME Corporation Malaysia, Small and Medium Enterprises Corporation Malaysia, MiGHT, Malaysian Industry Government Group of High Technology, Innovation Certificate, Enterprise Rating and Transformation, ISO 9001:2015, TUV Rheinland Cert GmbH, SCORE, SME Competitive Rating for Enhancement, Enterprise 50, SMIDEC, Golden Bull, Golden Bull 2007, Golden Bull 2006, Golden Bull 2005, Nanyang Siang Pau, Deloitte, Technology Fast 500 Asia Pacific 2006",
        'description': "TT Vision's Awards and Achievement"
    }

    return render(request, 'pages/award.html',context)

def event(request,slug):

    events = EventNews.objects.filter(slug=slug).first()
    eventtitle = EventNews.objects.all()
    pe = PhotoEvent.objects.filter(postlib__slug=slug)
    company = Company.objects.get(id=1)
    context = {
        'title': events,
        'etitle':eventtitle,
        'e':events,
        'pe':pe,
        'com':company,
        'keywords':"events",
        'description':"TT Vision's Past Events - "
    }
    return render(request, 'pages/event.html',context)

def news(request):
    company = Company.objects.get(id=1)
    nw = News.objects.all().order_by('created_at')
    page = request.GET.get('page',1)
    paginator = Paginator(nw,10)

    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)

   
    context = {
        'title': 'News',
        'news':newss,
        'com':company,
        'keywords':"news",
        'description':"TT Vision's News"
    }
    return render(request, 'pages/news.html',context)

def newslist(request):
    nw = News.objects.all().order_by('-created_at')
    page = request.GET.get('page',1)
    paginator = Paginator(nw,4)

    try:
        newss = paginator.page(page)
    except PageNotAnInteger:
        newss = paginator.page(1)
    except EmptyPage:
        newss = paginator.page(paginator.num_pages)

    company = Company.objects.get(id=1)
    context = {
        'title': 'News',
        'news':newss,
        'com':company,
        'keywords':"news",
        'description':"TT Vision's News - "
    }
    return render(request, 'pages/blog-list.html',context)

def press(request):
   
    pressl = Pressrelease.objects.all().order_by('created_at')
    company = Company.objects.get(id=1)
    context = {
        'title': 'Press Release',
        'press':pressl,
        'com':company,
        'keywords':"press releases, current affairs",
        'description':"TT Vision's Latest Press Releases and Affairs"
    }
    return render(request, 'pages/press.html',context)

def newsm(request):
    company = Company.objects.get(id=1)
    context = {
        'title': 'Media',
        'com':company,
        'keywords':"media",
        'description':"TT Vision's Media"
    }
    return render(request, 'pages/media.html',context)

#---------------------------old views-------------------------
# def robotic(request):
#     company = Company.objects.get(id=1)
#     context = {
#         'title': 'Advance Robotics Solutions',
#         'com':company,
#         'keywords':"autonomous mobile robot, Mobile robot, amr, autonomous mobile robot AMR, machine tending, fluid dispensing, wire mesh handling, assembly, collaborative, tester handling, machine vision, polishing, i4.0, auto welding, cobot, system integration, end effector, robotic, pick and place, auto packing, palletizing, warehouse automation, auto sanding, AGV, systems and iot",
#         'description':"TT Vision's Advance Robotic Solutions and Products: Robotic Machine Tending, Robotic Spot Welding, Robotic Pick & Place + Assembly, Cobot Dispensing, Cobot Test Handler, Robot Auto Packing, Mobile Robot Integration, Robot Palletizer"
#     }
#     return render(request, 'pages/robotic.html',context)
    
# def pvinspect(request):
#     company = Company.objects.get(id=1)
#     context = {
#         'title': 'PV Inspection, Test and Sort Solutions',
#         'com':company,
#         'keywords':"solar test and sort, solar sort, solar test, perovskite, Electroluminescence EL, machine vision, bottom cell, unloader, innovation, automation, solarpv, Transflection TF, solar wafer sorting, sorting, Photoluminescence PL, testing, top cell, loader, microcrack, handler",
#         'description':"TT Vision's PV Inspections, Test & Sort Solutions and Products: Solar Cell FRV-AOI, Solar Cell PL-AOI, Solar CEll TF-AOI, IBC Cell Sorter, Quad Cell Sorter",
#     }
#     return render(request, 'pages/inspectionlist.html',context)

def semiconductorlist(request):
    company = Company.objects.get(id=1)
    context = {
        'icled': True,
        'title': 'Semiconductor & LED Inspection Solutions',
        'com':company,
        'keywords':"automated optical inspection, wirebond aoi, substrate, vision module, LED, post tape, automated optical inspection, axi, optoelectronics, semiconductor aoi, package, 3D inspection, vision, wirebond, wafer, x-ray",
        'description':"TT Vision's Semiconductor/LED Inspection Solutions and Products: Substrate Package AOI Machine, Wafer AOI Machine, Wirebond AOI Machine"

    }
    return render(request, 'pages/semiconductorlist.html',context)

# def rpv(request, slug):

#     pr = Product.objects.get(productslug=slug)
#     company = Company.objects.get(id=1)

#     context = {
#         'title': pr,
#         'rpv':True,
#         'pr':pr,
#         'com':company
#     }
#     return render(request, 'pages/productviews.html',context)

# def pinspection(request, slug):

#     pr = Product.objects.get(productslug=slug)
#     company = Company.objects.get(id=1)

#     context = {
#         'title': pr,
#         'ins':True,
#         'pr':pr,
#         'com':company
#     }
#     return render(request, 'pages/productviews.html',context)

def icled(request, slug):
    pr = Product.objects.get(productslug=slug)
    company = Company.objects.get(id=1)
    context = {
        'title': pr,
        'icled':True,
        'pr':pr,
        'com':company
    }

    return render(request, 'pages/productviews.html',context)

#---------------------------new views-------------------------
#robotic mainpage
def robotic(request):
    cat = Category.objects.get(category='Robotic')
    pr = Product.objects.filter(productcategory = cat, status = True)
    company = Company.objects.get(id=1)
    context = {
        'pr': pr,
        'rpv': True,
        'title': 'Advance Robotics Solutions',
        'com':company,
        'keywords':"autonomous mobile robot, Mobile robot, amr, autonomous mobile robot AMR, machine tending, fluid dispensing, wire mesh handling, assembly, collaborative, tester handling, machine vision, polishing, i4.0, auto welding, cobot, system integration, end effector, robotic, pick and place, auto packing, palletizing, warehouse automation, auto sanding, AGV, systems and iot",
        'description':"TT Vision's Advance Robotic Solutions and Products: Robotic Machine Tending, Robotic Spot Welding, Robotic Pick & Place + Assembly, Cobot Dispensing, Cobot Test Handler, Robot Auto Packing, Mobile Robot Integration, Robot Palletizer"
    }
    return render(request, 'pages/productmainpage.html',context)

#robotic product page
def rpv(request, slug):
    pr = Product.objects.get(productslug=slug)
    fea = Productfeas.objects.filter(product = pr)
    company = Company.objects.get(id=1)

    context = {
        'title': pr,
        'rpv': True,
        'pr': pr,
        'com':company,
        'f': fea
    }
    return render(request, 'pages/productviews.html',context)

#solar mainpage
def pvinspect(request):
    cat = Category.objects.get(category='PV-Inspection')
    pr = Product.objects.filter(productcategory = cat, status = True)
    company = Company.objects.get(id=1)
    context = {
        'ins': True,
        'pr': pr,
        'title': 'PV Inspection, Test and Sort Solutions',
        'com':company,
        'keywords':"solar test and sort, solar sort, solar test, perovskite, Electroluminescence EL, machine vision, bottom cell, unloader, innovation, automation, solarpv, Transflection TF, solar wafer sorting, sorting, Photoluminescence PL, testing, top cell, loader, microcrack, handler",
        'description':"TT Vision's PV Inspections, Test & Sort Solutions and Products: Solar Cell FRV-AOI, Solar Cell PL-AOI, Solar CEll TF-AOI, IBC Cell Sorter, Quad Cell Sorter",
    }
    return render(request, 'pages/productmainpage.html',context)

#solar product page
def pinspection(request, slug):

    pr = Product.objects.get(productslug=slug)
    fea = Productfeas.objects.filter(product = pr)
    company = Company.objects.get(id=1)

    context = {
        'title': pr,
        'ins':True,
        'pr':pr,
        'com':company,
        'f': fea
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
    company = Company.objects.get(id=1)
    meta = Metapro.objects.get(position=6)

    context = {
        'title':'Investor Relation - Announcements',
        'iv':iv,
        'bursa':b,
        'com':company,
        'meta':meta,
        'keywords':"investor relation, bursa, bursa malaysia, ace market, stocks",
        'description':"TT Vision's Investor Relations Announcment"
    }
    return render(request, 'pages/invester.html',context)

def leapmarket(request):

    b = Category.objects.filter(catype=1)
    company = Company.objects.get(id=1)
    meta = Metapro.objects.get(position=8)
    
    url = 'https://www.bursamalaysia.com/api/v1/announcements/search?ann_type=company&company=03020&per_page=50&page=1&_=1672847484446'
    res = requests.get(url)
    data = res.json()

    p  = data['data']


    context = {
        'title':'Investor Relation - Announcements:LEAP Market',
        'bursa':b,
        'com':company,
        'data':p,
        'meta':meta,
        'noindex':True
    }

    return render(request, 'pages/leap-market.html',context)

def acemarket(request):


    url = 'https://www.bursamalaysia.com/api/v1/announcements/search?ann_type=company&company=0272&per_page=50&page=1&_=1672995464303'
    res = requests.get(url)
    data = res.json()
    meta = Metapro.objects.get(position=4)

    p = data['data']

    b = Category.objects.filter(catype=1)
    company = Company.objects.get(id=1)

    context = {
        'title':'Investor Relation - Announcements:ACE Market',
        'bursa':b,
        'com':company,
        'data':p,
        'meta':meta,
    }

    return render(request, 'pages/ace-market.html',context)  

def meetings(request):

    iv = AnnoucementMeetings.objects.all()
    b = Category.objects.filter(catype=5)
    company = Company.objects.get(id=1)

    context = {
        'title':'Meetings',
        'iv':iv,
        'bursa':b,
        'com':company,
        'keywords':'EGM, meetings',
        'description':"TT Vision's Meeting Announcements"
    }
    return render(request, 'pages/mettings.html',context)

def career(request):

    company = Company.objects.get(id=1)
    meta = Metapro.objects.get(position=5)

    context = {
        'title':'Careers',
        'com':company,
        'meta':meta,
        'keywords':"job, full time job, internship, intern, career, software and control engineer, mechanical design engineer, project engineer, project coordinator, software development engineer, r&d engineer, application engineer, it engineer, shipping clerk, admin clerk, mechanical engineer, e&e engineering, electrical and electronic engineering, mechatronics engineering, computer engineering, it engineering, software engineering",
        'description':"TT Vision's Careers and Open Job Positions"
    }
    return render(request, 'pages/career.html',context)


def callinaction(request):
    meta = Metapro.objects.get(position=7)
    company = Company.objects.get(id=1)

    context = {
        'title': 'Enquiry',
        'meta':meta,
        'com':company,
        'keywords':"contact, enquiry",
        'description': "TT Vision's Enquiry Page Regarding Investor Relations"
    }
    return render(request, 'pages/callinaction.html',context)

def fr(request):
    company = Company.objects.get(id=1)

    context = {
        'title': 'Quarterly Report',
        'com':company,
        'keywords':"financial report, financial summary, ipo factsheet",
        'description': "TT Vision's Quarterly Financial Report and Summary"
    }
    return render(request, 'pages/fr.html',context)

def term(request):
    company = Company.objects.get(id=1)

    context = {
        'title': 'Terms and Conditions',
        'com':company,
        'keywords':"terms and conditions, terms, conditions",
        'description': "TT Vision's Website Terms and Conditions"
    }
    return render(request, 'pages/privacy.html',context)


def mediakit(request):

    company = Company.objects.get(id=1)

    context = {
        'title': 'Media',
        'com':company,
        'keywords':"news media, media coverage, news coverage",
        'description': "TT Vision's News and Media Coverage"
    }
    return render(request, 'pages/media.html',context)


def coporategovernage(request):

    company = Company.objects.get(id=1)

    context = {
        'title': 'Corporate Governance',
        'com':company,
        'keywords':"corporate governance, board charter, audit & risk management committee, remuneration committee, nomination committee, code of conduct & Ethics, Anti-bribery, anti-corruption, whistleblowing, fit and proper policy, remuneration policy, remuneration, remuneration procedure",
        'description': "TT Vision's Corporate Governance"
    }

    return render(request, 'pages/corporate-governace.html',context)

def agmegm(request):


    company = Company.objects.get(id=1)

    context = {
        'title': 'Shareholders Meeting (AGM/EGM)',
        'com':company,
        'keywords':"agm, egm, meeting, shareholder, shareholder's meeting",
        'description': "TT Vision's Shareholders' Meeting"
    }

    return render(request, 'pages/agmegm.html',context)


def annualreport(request):


    company = Company.objects.get(id=1)

    context = {
        'title': 'Annual Report',
        'com':company,
        'keywords':"annual report, financial report, financial summary",
        'description': "TT Vision's Annual Financial Report and Summary"
    }

    return render(request, 'pages/annualreport.html',context)

#Job application page
def hrForm(request):
    company = Company.objects.get(id=1)
    meta = Metapro.objects.get(position=3)

    if request.method == 'POST':
        form = HrForm(request.POST, request.FILES)
       
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Send an email with the form data
            #check which job type he is applying for
            if form.cleaned_data["jobtype"] == 'Full Time':
                job = form.cleaned_data["fulltime"]
            elif form.cleaned_data["jobtype"] == 'Internship':
                job = form.cleaned_data["internship"]

            #email contents
            subject = 'Job Application for ' + job 
            message = f'Name: {form.cleaned_data["contactname"]}\nEmail: {form.cleaned_data["contactemail"]}\nPhone Number: {form.cleaned_data["contacttel"]}\nCountry: {form.cleaned_data["country"]}\nJob Position Applied: {job} ({form.cleaned_data["jobtype"]})'
            # resume = form.cleaned_data["resume"]
            # appform = form.cleaned_data["appform"]
            #domain email
            from_email = settings.SERVER_EMAIL
            #recipient email
            #recipient_list = ['hr@ttvision-tech.com']
            recipient_list = ['adriannasim@gmail.com']
            #attaching contents to the email to be sent
            email = EmailMessage(subject, message, from_email, recipient_list)
            #attaching files to email
            fname = form.cleaned_data["contactname"]
            fname = fname.replace(' ', '_')
            rpath = os.path.join(settings.MEDIA_ROOT, f'resume/resume-{fname}.pdf')
            apath = os.path.join(settings.MEDIA_ROOT, f'resume/applicationform-{fname}.pdf')

            email.attach_file(rpath)
            email.attach_file(apath)

            email.send()
            #redirect to success
            return redirect('contactdone')
        else:
            print(form.errors)
            print('Failed to send')
    else:
        form = HrForm()

    context = {
        'title': 'Contact Us',
        'form':form,
        'com':company,
        'meta':meta,
        'keywords': "contact, contact us, location, tel, telephone, email, fax, phone, sales@ttvision-tech.com, 604-6456294, 604-6456295",
        'description': "Contact Us At Email: 'sales@ttvision-tech.com' | Tel: 604-6456294 | Fax:604-6456295 | Location: Plot 106, Hilir Sungai Keluang 5, Bayan Lepas Phase 4, 11900, Penang, Malaysia"
    }

    return render(request, 'pages/hrform.html', context)