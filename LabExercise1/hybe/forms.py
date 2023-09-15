from django import forms  
from hybe.models import Artist  
class ArtistForm(forms.ModelForm):  
    class Meta:  
        model = Artist 
        fields = ['img', 'birthname', 'stagename', 'birthdate', 'age'] 
        widgets = { 'img': forms.ClearableFileInput(attrs={ 'class': 'form-control' }),
            'birthname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'stagename': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'birthdate': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date' }), 
            'age': forms.TextInput(attrs={ 'class': 'form-control' }),
      }