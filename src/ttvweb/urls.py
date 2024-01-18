"""ttvweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from web import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('term-and-condition',views.term, name="term"),
    path('', views.index, name='index' ),
    path('contact-us',views.contactus, name="contact"),
    path('contact-us/success',views.contactdone, name="contactdone"),
    path('company-background',views.companybackground, name="cb"),
    path('award', views.award, name="award"),
    path('event/<str:slug>', views.event, name="event"),
    path('news', views.news, name="news"),
    path('meetings',views.meetings, name='meetings'),
    path('financial-report',views.fr, name='fr'),
    path('news-list',views.newslist, name="newslist"),
    path('press-release', views.press, name="press"),
    path('newsm', views.newsm, name="newsm"),
#-----------------------------Product-----------------------------
    path('robotic',views.robotic, name="robotic"),
    path('robotic/<str:slug>', views.rpv, name="robotic"),
    path('pvinspect',views.pvinspect, name="pvinspect"),
    path('pvinspect/<str:slug>',views.pinspection, name="pvinspect"),
    path('semiconductorlist', views.semiconductorlist, name="semiconductorlist"),
    path('semiconductorlist/<str:slug>',views.icled, name="semiconductorlist"),

    path('investor-relation/announcement', views.investor, name="investor"),
    path('investor-relation/announcement/leap-market', views.leapmarket, name="leapmarket"),
    path('investor-relation/announcement/ace-market',views.acemarket,name='acemarket'),
    path('investor-relation/enquiry',views.callinaction, name="callinaction"),
    path('investor-relation/corporate-governance',views.coporategovernage, name="cg"),
    path('investor-relation/shareholdermeetings',views.agmegm, name="agmegm"),
    path('investor-relation/annual-report',views.annualreport, name="ar"),
    
    path('newsletter', views.newsletter, name='newletter'),
    path('news-media', views.media, name='medialink'),
#----------------------------job application page----------------------------
    path('hrform', views.hrForm, name='hrform'),
    path('hrform/success',views.contactdone, name="contactdone"),
#------------------------------Career page-------------------------------
    path('career',views.career, name="career"),

    #tests
    3path('test', views.media, name='test'),
    # path('test-robotics-mainpage/<str:slug>', views.trpv, name="test-robotics-mainpage"),
    #path('test-career',views.career, name="test-career"),

    #not in use
    # path('mission-vision',views.vision, name="vision"),
    # path('semiconductor', views.semiconductor, name="semiconductor"),
    # path('pv-inspections', views.pv, name="pv"),
    # path('semiconductor/wafer-and-package-AOI',views.semi1, name="semi1"),
    # path('semiconductor/wirebond-AOI-Equipment',views.semi2, name="semi2"),
    # path('semiconductor/Substrate-Package-AOI',views.semi3, name="semi3"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
