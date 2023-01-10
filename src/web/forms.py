from django import forms
from django.db import models
from .models import Contact, Newsletter
from django_countries import Countries
from django.db.models.fields import BLANK_CHOICE_DASH


class NewsletterForm(forms.ModelForm):
    
    mailaddress = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name Here'}))
    newname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name Here'}))
    company  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name Here'}))

    class Meta:
        model = Newsletter
        fields = [
            'mailaddress',
            'newname',
            'company',
        ]

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

    CON = Countries

    contactname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name Here'}))
    contactemail = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email Here'}))
    companyname = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please insert your company name'}))
    looking = forms.ChoiceField(choices=Find, required=False, widget=forms.Select(attrs={'class':'form-control'}))
    country = forms.ChoiceField(choices=CON, required=False, widget=forms.Select(attrs={'class':'form-control'}))
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