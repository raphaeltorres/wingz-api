from rest_framework import mixins, viewsets, generics, filters
from django_filters import rest_framework as django_filters
from django.utils.timezone import now, timedelta
from django.db.models import Prefetch

from .models import User, Ride, RideEvent
from .serializers import UserSerializer, RideSerializer, RideEventSerializer
from ride.pagination import ResultsSetPagination
from .filters import RideFilter

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for managing User instances.
    Supports listing, creating, updating, retrieving, and deleting users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RideViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for managing Ride instances.
    Supports listing, creating, updating, retrieving, and deleting rides.
    Includes pagination, filtering, and ordering.
    """
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    pagination_class = ResultsSetPagination
    filterset_class = RideFilter
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['pickup_time']
    ordering = ['pickup_time']

    def get_queryset(self):
        """
        Prefetch related ride events from the last 24 hours.
        """
        current_time = now() - timedelta(hours=24)
        
        current_events = RideEvent.objects.filter(
            created_at__gte=current_time
        ).order_by('-created_at')
        
        queryset = Ride.objects.select_related("id_driver", "id_rider").prefetch_related(
            Prefetch("events", queryset=current_events, to_attr="current_ride_events")
        )
        return queryset

class RideEventViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                       mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for managing RideEvent instances.
    Supports listing, creating, updating, retrieving, and deleting ride events.
    """
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer