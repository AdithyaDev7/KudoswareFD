from django import forms
from .models import Details

# we are creating a form for easy convertion into table format in html file
class DetailForm(forms.ModelForm):
    class Meta:
        model=Details
        fields='__all__'
        