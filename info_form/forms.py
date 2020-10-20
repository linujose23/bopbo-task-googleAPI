from django import forms
from . models import Contact
from django.forms import ClearableFileInput


# class Contact_form(forms.Form):
#     Name = forms.CharField(max_length=100, label='Enter Name')
#     Email = forms.EmailField(max_length=254)
#     Mobile = forms.CharField(max_length=12)
#     Message = forms.TextField(max_length=400)
#     Attachment = forms.FileField(upload_to='uploads/%Y/%m/%d/')

class Contact_form(forms.ModelForm):
    """
    docstring
    """
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Contact
        fields = ('Name', 'Email', 'Mobile', 'Message')
        # exclude = ('files',)
