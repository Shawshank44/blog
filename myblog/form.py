from django import forms
from django.db.models import fields
from .models import Comment

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']