from django import forms
from blogpost.models import Blogpost


class BlogpostForm(forms.ModelForm):

    class Meta:
        model = Blogpost
        fields = ['title', 'content']
