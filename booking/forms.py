from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'booked_by', 'date', 'start_time', 'end_time']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'booked_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อผู้จอง'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        room = cleaned_data.get('room')
        date = cleaned_data.get('date')
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')
        if start and end and start >= end:
            raise ValidationError('เวลาเริ่มต้องน้อยกว่าเวลาสิ้นสุด')
        conflicts = Booking.objects.filter(
            room=room, date=date,
            start_time__lt=end, end_time__gt=start
        )
        if conflicts.exists():
            raise ValidationError('ช่วงเวลานี้มีการจองซ้อนแล้ว')
        return cleaned_data