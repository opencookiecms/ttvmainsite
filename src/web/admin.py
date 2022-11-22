from multiprocessing.dummy import Event
from django.contrib import admin

from web.models import Accordation, Annoucement, Category, Company, Contact, EventNews, Heroseven, Herosix, Herotypefive, Herotypefour, Herotypeone, Herotypethree, Herotypetwo, News, PhotoEvent, PhotoLib, Post, Postsection, Product, Slide, Smallcard, Timeline, AnnoucementMeetings

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

