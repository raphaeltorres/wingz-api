from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from .models import User, Ride, RideEvent
from .serializers import UserSerializer
from .serializers import RideSerializer
from .serializers import RideEventSerializer
from ride.pagination import ResultsSetPagination
from .filters import RideFilter
from django_filters import rest_framework as django_filters

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RideViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    pagination_class = ResultsSetPagination
    filterset_class = RideFilter
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ['pickup_time']
    ordering = ['pickup_time']

class RideEventViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer