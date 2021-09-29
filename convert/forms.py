from django import forms 
from .models import *
  
class Upload(forms.ModelForm): 
  
    class Meta: 
        model =  UploadFile
        fields = '__all__'
