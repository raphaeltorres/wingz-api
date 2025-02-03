from rest_framework import mixins, generics
from rest_framework.response import Response
from .models import User, Ride, RideEvent
from .serializers import UserSerializer
from .serializers import RideSerializer
from .serializers import RideEventSerializer
from rest_framework import viewsets

class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RideViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  viewsets.GenericViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RideEventViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                  viewsets.GenericViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer