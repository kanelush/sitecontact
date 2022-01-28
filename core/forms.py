from django import forms
from .models import ContactForm


class ContactModelForm(forms.ModelForm):
    CHOICES = ((' ', ' '),('9:00', '9:00 horas'),('10:00', '10:00 horas'),('11:00', '11:00 horas'), ('12:00', '12:00 horas'), ('13:00', '13:00 horas'))
    fieldo = forms.ChoiceField(choices=CHOICES)
    
    class Meta:
        model = ContactForm
        fields = [
            'name', 
            'subject', 
            'description',
            'start_date',
            'fieldo',
            'mail',
            
        ]