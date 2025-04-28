from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import BookingForm
from django.db.models import Q

# รายการห้องทั้งหมด
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'rooms': rooms})

# สร้าง/แก้ไขการจอง
def booking_create(request, pk=None):
    if pk:
        booking = get_object_or_404(Booking, pk=pk)
    else:
        booking = None
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_form.html', {'form': form})

# แสดงรายการจอง พร้อมค้นหา
def booking_list(request):
    q = request.GET.get('q', '')
    room_filter = request.GET.get('room', '')
    date_filter = request.GET.get('date', '')
    bookings = Booking.objects.all()
    if q:
        bookings = bookings.filter(booked_by__icontains=q)
    if room_filter:
        bookings = bookings.filter(room_id=room_filter)
    if date_filter:
        bookings = bookings.filter(date=date_filter)
    rooms = Room.objects.all()
    return render(request, 'booking/booking_list.html', {
        'bookings': bookings, 'rooms': rooms,
        'q': q, 'room_filter': room_filter,
        'date_filter': date_filter
    })

# ยกเลิกการจอง
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})