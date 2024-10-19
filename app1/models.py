# proj1/models.py
from django.db import models

class Booking(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family')
    ]
    
    ROOM_PREFERENCE_CHOICES = [
        ('with_ac', 'With AC'),
        ('without_ac', 'Without AC')
    ]

    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    room_preference = models.CharField(max_length=10, choices=ROOM_PREFERENCE_CHOICES)
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Booking by {self.name} on {self.check_in}"
