from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

# Create your models here.

class Category(models.Model):

    CAT_ONE = 1
    CAT_TWO = 2
    CAT_THREE = 3
    CAT_FOR = 4
    CAT_FIVE = 5
    CAT_CHOICES = [
        (CAT_ONE, _("Bursa")),
        (CAT_TWO, _("Post")),
        (CAT_THREE, _("Product")),
        (CAT_FOR, _("News")),
        (CAT_FIVE, _("Meetings")),
    ]
   
    category = models.CharField(max_length=100, null=True, blank=True)
    catype = models.PositiveSmallIntegerField(choices=CAT_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.category

#-------------------old product model-----------------------
# class Product(models.Model):
#     producttitle = models.CharField(max_length=100, null=True, blank=True)
#     productslug =  models.CharField(max_length=200, null=True, blank=True)
#     productcategory = models.ForeignKey(Category, blank=True, null=True, on_delete = models.SET_NULL)
#     productimg = models.ImageField(null=True, blank=True)
#     productfea  = models.TextField(null=True, blank=True)
#     productspec  = models.TextField(null=True, blank=True)
#     status = models.BooleanField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)


#     def __str__(self):
#         return self.producttitle

#-------------------new product model-----------------------
class Product(models.Model):
    producttitle = models.CharField(max_length=100, null=True, blank=True)
    productintro = models.TextField(null=True, blank=True)
    productdesc = models.TextField(null=True, blank=True)
    productslug =  models.CharField(max_length=200, null=True, blank=True)
    productcategory = models.ForeignKey(Category, blank=True, null=True, on_delete = models.SET_NULL)
    productimg = models.ImageField(null=True, blank=True)
    productspec  = models.TextField(null=True, blank=True)
    status = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.producttitle

class Productfeas(models.Model):
    features = models.CharField(max_length=400, null=True, blank=True)
    featuresdesc = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    featureno = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        # Increment the feature count only when creating a new instance
        if not self.pk:
            existingNo = Productfeas.objects.filter(product=self.product).count()
            self.featureno = existingNo + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.producttitle} Feature {self.featureno}"

#update featureno    
@receiver(pre_save, sender=Productfeas)
def update_featureno(sender, instance, **kwargs):
    if not instance.pk:
        existingNo = Productfeas.objects.filter(product=instance.product).count()
        instance.featureno  = existingNo + 1
    
class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    postcategory = models.ForeignKey(Category, blank=True, null=True, on_delete = models.SET_NULL)
    postxtracontent = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    postimg = models.ImageField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

class Postsection(models.Model):
    smtitle = models.CharField(max_length=100, null=True, blank=True)
    bgtitle  = models.CharField(max_length=100, null=True, blank=True)
    picture1 = models.ImageField(null=True, blank=True)
    picture2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.bgtitle

class News(models.Model):
    titles = models.CharField(max_length=150, null=True, blank=True)
    titlecon = models.CharField(max_length=400, null=True, blank=True)
    newsdate = models.CharField(max_length=100, null=True, blank=True) 
    links  = models.CharField(max_length=250, null=True, blank=True)
    wowdelay = models.CharField(max_length=20, null=True, blank=True)
    newspicture = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position  = models.IntegerField(null=True, blank=True)
    ct = models.ForeignKey(Category, blank=True, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.titles

class EventNews(models.Model):
    ttitle = models.CharField(max_length=150, null=True, blank=True)
    eventtitle = models.CharField(max_length=200, null=True, blank=True)
    eventcontent = models.TextField(null=True, blank=True)
    eventpic = models.ImageField(null=True, blank=True)
    eventlink = models.CharField(max_length=150, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True) 
    url = models.CharField(max_length=150, null=True, blank=True)

    
    def __str__(self):
        return self.ttitle

class Annoucement(models.Model):
    anoncetitle = models.CharField(max_length=150, null=True, blank=True)
    stockname = models.CharField(max_length=150, null=True, blank=True)
    companyname = models.CharField(max_length=150, null=True, blank=True)
    andescription = models.TextField(null=True, blank=True)
    anousetype = models.CharField(max_length=50, null=True, blank=True)
    ansubject = models.CharField(max_length=150, null=True, blank=True)
    adlink = models.CharField(max_length=300, null=True, blank=True)
    andate = models.DateField(null=True, blank=True)
    anslug = models.CharField(max_length=200, null=True, blank=True)
    anpostimg = models.ImageField(blank=True, null=True)
    anmstatus = models.BooleanField(blank=True, null=True)
    ancategory = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    ancreated_at = models.DateTimeField(auto_now_add=True, editable=False)
    anupdated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.anoncetitle


class AnnoucementMeetings(models.Model):
    anoncetitle = models.CharField(max_length=150, null=True, blank=True)
    stockname = models.CharField(max_length=150, null=True, blank=True)
    companyname = models.CharField(max_length=150, null=True, blank=True)
    andescription = models.TextField(null=True, blank=True)
    anousetype = models.CharField(max_length=50, null=True, blank=True)
    ansubject = models.CharField(max_length=150, null=True, blank=True)
    adlink = models.CharField(max_length=300, null=True, blank=True)
    andate = models.DateField(null=True, blank=True)
    anslug = models.CharField(max_length=200, null=True, blank=True)
    anpostimg = models.ImageField(blank=True, null=True)
    anmstatus = models.BooleanField(blank=True, null=True)
    ancategory = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    ancreated_at = models.DateTimeField(auto_now_add=True, editable=False)
    anupdated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.anoncetitle




class PhotoLib(models.Model):
    imgtitle =  models.CharField(max_length=20, null=True,blank=True)
    img = models.ImageField(null=True, blank=True)
    postlib = models.ForeignKey(Post, blank=True, null=True,on_delete = models.SET_NULL)

class PhotoEvent(models.Model):
    imgtitle =  models.CharField(max_length=150, null=True,blank=True)
    imgtitle2 = models.CharField(max_length=150, null=True,blank=True)
    img = models.ImageField(null=True, blank=True)
    wowdelay = models.CharField(max_length=10, null=True,blank=True)
    postlib = models.ForeignKey(EventNews, blank=True, null=True,on_delete = models.SET_NULL)

    def __str__(self):
        return self.imgtitle


class Company(models.Model):
    companyname = models.CharField(max_length=100, null=True, blank=True)
    phonenumber = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    biglogo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.companyname

class Slide(models.Model):
    smtitle  = models.CharField(max_length=50, null=True, blank=True) 
    bgtitle = models.CharField(max_length=150, null=True, blank=True) 
    slidecontet = models.TextField(null=True, blank=True) 
    picture = models.ImageField(null=True, blank=True)
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.bgtitle

class Smallcard(models.Model):
    titletxt = models.CharField(max_length=100, null=True, blank=True)
    cardcontent = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True) 
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    cssclass = models.CharField(max_length=150, null=True, blank=True) 
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.titletxt

class Herotypeone(models.Model):
    transtext = models.CharField(max_length=20, null=True, blank=True)
    titletxt = models.CharField(max_length=20, null=True, blank=True)
    txtanimator = models.TextField(null=True, blank=True) 
    herocontent = models.TextField(null=True, blank=True) 
    experiance = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titletxt

class Herotypetwo(models.Model):

    txttitle = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    content1  = models.TextField(null=True, blank=True) 
    content2  = models.TextField(null=True, blank=True) 
    content3  = models.TextField(null=True, blank=True) 
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.txttitle

class Herotypethree(models.Model):
    txtitle = models.CharField(max_length=100, null=True, blank=True)
    icon1 = models.CharField(max_length=150, null=True, blank=True)
    imgtxt1 = models.CharField(max_length=50, null=True, blank=True)
    img1 = models.ImageField(null=True, blank=True)
    icon2 = models.CharField(max_length=150, null=True, blank=True)
    imgtxt2 = models.CharField(max_length=50, null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.txtitle

class Herotypefour(models.Model):
    bigtitle = models.CharField(max_length=50, blank=True, null=True)
    smalltitle = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(null=True, blank=True) 
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    transani = models.CharField(max_length=20, blank=True, null=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.bigtitle

class Herotypefive(models.Model):
    smtitle  = models.CharField(max_length=50, blank=True, null=True)
    bgtitle = models.CharField(max_length=50, blank=True, null=True)
    herocontent  = models.TextField(null=True, blank=True) 
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    transani = models.CharField(max_length=20, blank=True, null=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.smtitle

class Herosix(models.Model):
    smtitle  = models.CharField(max_length=50, blank=True, null=True)
    bgtitle = models.CharField(max_length=50, blank=True, null=True)
    content1  = models.TextField(null=True, blank=True)
    img1 = models.ImageField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    content3 = models.TextField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    content4 = models.TextField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)
    content5 = models.TextField(null=True, blank=True) 
    img5 = models.ImageField(null=True, blank=True)
    content6 = models.TextField(null=True, blank=True)
    img6 = models.ImageField(null=True, blank=True)
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    transani = models.CharField(max_length=20, blank=True, null=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.smtitle

class Heroseven(models.Model):
    smtitle  = models.CharField(max_length=50, blank=True, null=True)
    
    bgtitle1 = models.CharField(max_length=50, blank=True, null=True)
    content1  = models.TextField(null=True, blank=True)
    img1 = models.ImageField(null=True, blank=True)
   
    bgtitle2 = models.CharField(max_length=50, blank=True, null=True)
    content2 = models.TextField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    
    bgtitle3 = models.CharField(max_length=50, blank=True, null=True)
    content3 = models.TextField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    
    bgtitle4 = models.CharField(max_length=50, blank=True, null=True)
    content4 = models.TextField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)
    
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    transani = models.CharField(max_length=20, blank=True, null=True)
    link1 = models.CharField(max_length=200, null=True, blank=True)
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.smtitle
    


class Accordation(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    opentitle = models.TextField(blank=True, null=True)
    labelbyid = models.CharField(max_length=20, blank=True, null=True)
    toggle = models.CharField(max_length=20, blank=True, null=True)
    bstarget = models.CharField(max_length=20, blank=True, null=True)
    bsparent = models.CharField(max_length=20, blank=True, null=True)
    cat = models.ForeignKey(Category, blank=True, null=True,on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(null=True,blank=True)
    cssclass = models.CharField(max_length=200, null=True, blank=True)
    positionhero = models.CharField(max_length=20, null=True, blank=True)
    ariaexpanded = models.CharField(max_length=10, null=True, blank=True)
    sortnumber = models.IntegerField(null=True, blank=True)
    show = models.CharField(null=True, blank=True, max_length=10)


    def __str__(self):
        return self.title

class Contact(models.Model):
    contactname = models.CharField(max_length=50, null=True, blank=True)
    companyname = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    contactemail = models.CharField(max_length=50, null=True, blank=True)
    contacttel = models.CharField(max_length=50, null=True, blank=True)
    contactaddress = models.TextField(blank=True, null=True)
    looking = models.CharField(max_length=50, null=True, blank=True)
    enquirytype = models.CharField(max_length=50, null=True, blank=True)
    enquirysubject = models.CharField(max_length=150, null=True, blank=True)
    enquirycontent = models.TextField(blank=True, null=True)

class Timeline(models.Model):
    timelinename = models.CharField(max_length=50, null=True, blank=True)
    yearsstring = models.CharField(max_length=20, null=True, blank=True)
    thetitle = models.CharField(max_length=150, null=True, blank=True)
    thedescription = models.TextField(blank=True, null=True)
    position  = models.IntegerField(null=True, blank=True)


class Newsletter(models.Model):
    mailaddress = models.CharField(max_length=150, null=True, blank=True)
    newname = models.CharField(max_length=150, null=True, blank=True)
    company  = models.CharField(max_length=150, null=True, blank=True)


class Pressrelease(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    decs = models.CharField(max_length=500, null=True, blank=True)
    link = models.CharField(max_length=150, null=True, blank=True)
    datess = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position  = models.IntegerField(null=True, blank=True)

class Metapro(models.Model):
    urlcontent = models.CharField(max_length=150, null=True, blank=True)
    typecontent = models.CharField(max_length=150, null=True, blank=True)
    titlecontent = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    imagelink = models.CharField(max_length=150, null=True, blank=True)
    position  = models.IntegerField(null=True, blank=True)

#Job application form
#filenames
def rfilepath (instance, filename):
    return os.path.join('resume',f'resume-{instance.contactname}.pdf')

def afilepath (instance, filename):
    return os.path.join('resume',f'applicationform-{instance.contactname}.pdf')

class Hr(models.Model):
    contactname = models.CharField(max_length=100, null=False, blank=False)
    contactemail = models.EmailField(null=False, blank=False)
    jobtype = models.CharField(max_length=20, null=False, blank=False)
    fulltime = models.CharField(max_length=50, null=True, blank=True)
    internship = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=False, blank=False)
    contacttel = models.CharField(max_length=20, null=False, blank=False)
    resume = models.FileField(upload_to=rfilepath)
    appform = models.FileField(upload_to=afilepath)

#job positions
class Job(models.Model):
    jobname = models.CharField(max_length=100, null=False, blank=False)
    jobdesc = models.TextField(null=False, blank=False)
    joblink = models.CharField(max_length=400, null=False, blank=False)