from django import forms
from .models import Shipments

class AddShipmentsForm(forms.Form):
    destination=forms.CharField(label="Destination")
    weight=forms.IntegerField(label="Weight")

class fform(forms.Form):
    origin=forms.CharField(label="ADD THE ORIGIN")
    weight=forms.IntegerField(label="ADD MAX WT OF CARRIER")  
