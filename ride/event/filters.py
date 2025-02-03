from django_filters import rest_framework as filters
from .models import User, Ride

# Custom filter class
class RideFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='iexact') 
    rider_email = filters.CharFilter(field_name='id_rider__email', lookup_expr='icontains') 

    class Meta:
        model = Ride
        fields = ['status', 'id_rider__email']