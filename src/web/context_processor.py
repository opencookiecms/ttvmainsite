import requests
from .forms import NewsletterForm



def Newform(request):
    form = NewsletterForm

    return {'form2':form}
