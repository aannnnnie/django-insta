from django import forms
from .models import *


class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = "__all__"
