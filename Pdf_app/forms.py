from django import forms
from .models import PDFFile

class PDFUploadFile(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['file']
