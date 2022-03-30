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
    path('', views.index, name='index' ),
    path('company-background',views.companybackground, name="cb"),
    path('mission-vision',views.vision, name="vision"),
    path('award', views.award, name="award"),
    path('event/<str:slug>', views.event, name="event"),
    path('news', views.news, name="news"),
    path('press-release', views.news, name="press"),
    path('newsm', views.newsm, name="newsm"),
    path('semiconductor', views.semiconductor, name="semiconductor"),
    path('robotic',views.robotic, name="robotic"),
    path('pv-inspections', views.pv, name="pv"),
    path('robotic/robotic-machine-tending',views.robotic1, name="tending"),
    path('robotic/robotic-spot-welding',views.robotic2, name="welding"),
    path('robotic/robotic-pick-and-place',views.robotic3, name="pnp"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
