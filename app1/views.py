from django.shortcuts import render, redirect,get_object_or_404
from app1.forms import BookingForm
from .models import Booking

def index(request):
    return render(request, "index.html")

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the database
            return redirect('success', booking_id=booking.id)  # Redirect to success page with booking ID
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})

def success(request,booking_id=None):
    # Fetch all bookings from the database
    bookings = Booking.objects.all()
    
    context = {
        'bookings': bookings,
    }
    return render(request, 'success.html', context)
def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to success page without booking_id
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('success', booking_id=booking.id)  # Pass the booking_id
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'update_booking.html', {'form': form, 'booking': booking})
    pass
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        # Redirect to the success page without booking_id
        return redirect('success')
    
    return render(request, 'confirm_delete.html', {'booking': booking})