from django import forms
from .models import *


class Upload(forms.ModelForm):

    class Meta:
        model = UploadFile
        widgets = {
            "file":
            forms.FileInput(
                attrs={
                    'required': 'true',
                    "accept": "application/pdf",
                    "class": "form-control",
                    "aria-describedby": "button-addon1"
                })
        }
        fields = '__all__'
