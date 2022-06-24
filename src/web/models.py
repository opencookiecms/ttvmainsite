
from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    producttitle = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.producttitle

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
    titlecon = models.CharField(max_length=250, null=True, blank=True)
    newsdate = models.CharField(max_length=100, null=True, blank=True) 
    links  = models.CharField(max_length=200, null=True, blank=True)
    wowdelay = models.CharField(max_length=20, null=True, blank=True)
    newspicture = models.ImageField(null=True, blank=True)
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
    andescription = models.CharField(max_length=150, null=True, blank=True)
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
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
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
    link2 = models.CharField(max_length=200, null=True, blank=True)
    link3 = models.CharField(max_length=200, null=True, blank=True)
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
    contacttel = models.CharField(max_length=20, null=True, blank=True)
    contactaddress = models.TextField(blank=True, null=True)
    looking = models.CharField(max_length=50, null=True, blank=True)
    enquirytype = models.CharField(max_length=50, null=True, blank=True)
    enquirysubject = models.CharField(max_length=150, null=True, blank=True)
    enquirycontent = models.TextField(blank=True, null=True)











    
