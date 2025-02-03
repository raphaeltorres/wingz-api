from django.db import models

class User(models.Model):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        RIDER = 'rider', 'Rider'
        DRIVER = 'driver', 'Driver'
    
    id_user = models.AutoField(primary_key=True)  # Auto-incrementing integer primary key
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.ADMIN
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Optional phone number

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Ride(models.Model):
    class StatusChoices(models.TextChoices):
        EN_ROUTE = 'en-route', 'En Route'
        PICKUP = 'pickup', 'Pickup'
        DROPOFF = 'dropoff', 'Dropoff'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.EN_ROUTE
    )
    id_rider = models.ForeignKey('User', on_delete=models.CASCADE, related_name='rides_as_rider')
    id_driver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id_rider.first_name} - {self.status}"
    
class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey('Ride', on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['id_ride']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Event {self.id_ride_event} - Ride {self.id_ride.id_ride}"

