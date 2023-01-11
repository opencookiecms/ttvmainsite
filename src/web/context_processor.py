import requests
from .forms import NewsletterForm
from .models import Metapro



def Newform(request):
    form = NewsletterForm
    return {'form2':form}
