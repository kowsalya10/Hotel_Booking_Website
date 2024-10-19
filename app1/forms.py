from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    ROOM_PREFERENCE_CHOICES = [
        ('with_ac', 'With AC'),
        ('without_ac', 'Without AC')
    ]

    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family')
    ]

    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    room_preference = forms.ChoiceField(choices=ROOM_PREFERENCE_CHOICES, widget=forms.RadioSelect, label='Room Preference')
    room_type = forms.ChoiceField(choices=ROOM_TYPE_CHOICES, widget=forms.RadioSelect, label='Room Type')
    contact_number = forms.CharField(max_length=15, label='Contact Number')

    class Meta:
        model = Booking
        fields = ['name', 'contact_number', 'check_in', 'check_out', 'room_type', 'room_preference', 'special_requests']
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 4}),
        }
