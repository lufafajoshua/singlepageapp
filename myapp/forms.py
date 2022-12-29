from django import forms
from .models import Mydata

class DataForm(forms.ModelForm):
    class Meta:
        model = Mydata
        fields = ('name', 'age', 'telephone', 'gender', 'address', 'marital_status', 'email')

class SearchForm(forms.Form):
    search_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'form-name', 'name':'form-name', 'placeholder':'Search Data...'}))
