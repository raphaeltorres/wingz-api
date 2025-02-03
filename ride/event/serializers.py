from rest_framework import serializers
from .models import User, Ride, RideEvent

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['id_user', 'role', 'first_name', 'last_name', 'email', 'phone_number']

class RideEventSerializer(serializers.ModelSerializer):
    """
    Serializer for the RideEvent model.
    """
    class Meta:
        model = RideEvent
        fields = ['id_ride_event', 'id_ride', 'description', 'created_at']

class RideSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ride model.
    Includes nested UserSerializer for driver and rider details,
    and a method field for retrieving current ride events.
    """
    id_driver = UserSerializer(read_only=True)
    id_rider = UserSerializer(read_only=True)
    current_ride_events = serializers.SerializerMethodField()
    
    class Meta:
        model = Ride
        fields = [
            'id_ride', 'status', 'id_rider', 'id_driver',
            'pickup_latitude', 'pickup_longitude',
            'dropoff_latitude', 'dropoff_longitude', 'pickup_time',
            'current_ride_events'
        ]
    
    def get_current_ride_events(self, obj):
        """
        Retrieves and serializes the current ride events related to the ride instance.
        """
        return RideEventSerializer(obj.current_ride_events, many=True).data
        
