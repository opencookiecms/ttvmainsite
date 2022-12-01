from django import forms
from django.db import models
from .models import Contact
from django_countries import Countries

class ContactForm(forms.ModelForm):

    Find = (
        ('','Choose...'),
        ('Search Engine','Search Engine'),
        ('Linkedin','Linkedin'),
        ('Exhibition','Exhibition'),
        ('Email Newsletter','Email Newsletter'),
        ('Youtube','Youtube'),
        ('Others','Others'),
    )

    contactname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name Here'}))
    contactemail = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email Here'}))
    companyname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please insert your company name'}))
    looking = forms.ChoiceField(choices=Find, required=False, widget=forms.Select(attrs={'class':'form-control'}))
    country = forms.ChoiceField(choices=Countries, required=False, widget=forms.Select(attrs={'class':'form-control'}))
    contacttel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    enquirysubject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your subject enquiry here'}))
    enquirycontent = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Your Enquiry', 'rows':'4'}))
    class Meta:
        model = Contact
        fields = [
            'contactname', 
            'companyname', 
            'country', 
            'contactemail', 
            'contacttel',
            'contactaddress', 
            'looking', 
            'enquirytype',
            'enquirysubject',
            'enquirycontent', 

        ]