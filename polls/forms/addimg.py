from django import forms
from ..models import Userdet


class IMGdet(forms.ModelForm):
    class Meta:
        model = Userdet
        fields = ('userIMG',)