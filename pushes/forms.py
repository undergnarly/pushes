from django import forms
import datetime
from django.forms import ModelForm
from pushes.models import Pushes

class PushesForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField(initial=datetime.date.today)
    published = forms.BooleanField(required=False)
    
    
class PushesModelForm(ModelForm):    
    class Meta:
        model = Pushes
        fields = ['title', 'text', 'published_date']
