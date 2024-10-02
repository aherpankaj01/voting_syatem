from django import forms 

class NewForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    msg = forms.CharField(label='Message', max_length=200)