from multiprocessing.dummy import Event
from django.contrib import admin

from web.models import Accordation, Annoucement, Category, Company, Contact, EventNews, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, News, PhotoEvent, PhotoLib, Post, Postsection, Product, Productfeas, Slide, Smallcard, Timeline, AnnoucementMeetings, Newsletter ,Pressrelease, Metapro, Hr

#configs
class ProductfeasAdmin(admin.ModelAdmin):
#make the data in the category field persistent after clicking add another
    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" in request.POST:
            request.POST = request.POST.copy()
            request.POST['product'] = str(obj.product_id)
            return super().response_add(request, obj, post_url_continue)
        else:
            return super().response_add(request, obj)

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
admin.site.register(Product)
admin.site.register(Productfeas, ProductfeasAdmin)
admin.site.register(Accordation)
admin.site.register(PhotoLib)
admin.site.register(Postsection)
admin.site.register(Herosix)
admin.site.register(Heroseven)
admin.site.register(News)
admin.site.register(PhotoEvent)
admin.site.register(EventNews)
admin.site.register(Annoucement)
admin.site.register(Contact)
admin.site.register(Timeline)
admin.site.register(AnnoucementMeetings)
admin.site.register(Newsletter)
admin.site.register(Pressrelease)
admin.site.register(Metapro)
admin.site.register(Hr)