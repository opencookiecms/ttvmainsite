from multiprocessing.dummy import Event
from typing import Any
from django.contrib import admin

from web.models import Accordation, Annoucement, Category, Company, Contact, EventNews, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, News, PhotoEvent, Post, Postsection, Product, Productfeas, Productin, Productapp, Productspecs, Slide, Smallcard, Timeline, AnnoucementMeetings, Newsletter ,Pressrelease, Metapro, Hr, Job, Media, ReqForm

# Register your models here.
admin.site.register(Company)
admin.site.register(Slide)
admin.site.register(Smallcard)
admin.site.register(Herotypeone)
admin.site.register(Herotypetwo)
admin.site.register(Herotypethree)
admin.site.register(Herotypefour)
admin.site.register(Herotypefive)
admin.site.register(Post)
admin.site.register(Category)

#Create a formset of productfeas in product model at Django Admin
class ProductfeasInline(admin.TabularInline):
    model = Productfeas
    #Formset title
    verbose_name_plural = "Product Features"
    extra = 1

class ProductappInline(admin.TabularInline):
    model = Productapp
    #Formset title
    verbose_name_plural = "Product Applications"
    extra = 1

class ProductinInline(admin.TabularInline):
    model = Productin
    #Formset title
    verbose_name_plural = "Machines Integrated"
    extra = 1

class ProductspecInline(admin.StackedInline):
    model = Productspecs
    #Formset title
    verbose_name_plural = "Product Specifications"

#Register product model with all the formsets
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    inlines = [ProductfeasInline, ProductappInline, ProductinInline, ProductspecInline]

admin.site.register(Accordation)
#admin.site.register(PhotoLib)
admin.site.register(Postsection)
admin.site.register(Herosix)
admin.site.register(Heroseven)
admin.site.register(News)
admin.site.register(PhotoEvent)
#admin.site.register(EventNews)

#Event
class EventPhotosInline(admin.TabularInline):
    model = PhotoEvent
    extra = 1
@admin.register(EventNews)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventPhotosInline]

admin.site.register(Annoucement)
admin.site.register(Contact)
admin.site.register(Timeline)
admin.site.register(AnnoucementMeetings)
admin.site.register(Newsletter)
admin.site.register(Pressrelease)
admin.site.register(Metapro)
admin.site.register(Hr)
admin.site.register(Job)
admin.site.register(Media)
admin.site.register(ReqForm)

#configs
# class ProductfeasAdmin(admin.ModelAdmin):
# #make the data in the category field persistent after clicking add another
#     def response_add(self, request, obj, post_url_continue=None):
#         print("response add is called")
#         if "_addanother" in request.POST:
#             request.POST = request.POST.copy()
#             request.POST['product'] = str(obj.product.id)
#             return super().response_add(request, obj, post_url_continue)
#         else:
#             return super().response_add(request, obj)