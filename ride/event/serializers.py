from rest_framework import serializers
from .models import User
from .models import Ride
from .models import RideEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'role', 'first_name', 'last_name', 'email', 'phone_number']

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id_ride', 'status', 'id_rider', 'id_driver', 'pickup_latitude', 
                  'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 'pickup_time']
        
    def to_representation(self, obj):
        return {
                'id_ride': obj.id_ride,
                'status': obj.status,
                'id_rider': obj.id_rider.first_name + " " + obj.id_rider.last_name,
                'id_driver': obj.id_driver.first_name + " " + obj.id_driver.last_name,
                'pickup_latitude': obj.pickup_latitude,
                'pickup_longitude': obj.pickup_longitude,
                'dropoff_latitude': obj.dropoff_latitude,
                'dropoff_longitude': obj.dropoff_longitude,
                'pickup_time': obj.pickup_time
            }
        
class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = ['id_ride_event', 'id_ride', 'description', 'created_at']