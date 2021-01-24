from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))