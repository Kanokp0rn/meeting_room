from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room.name} booked by {self.booked_by} on {self.date}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'date', 'start_time', 'end_time'],
                name='unique_booking'
            )
        ]