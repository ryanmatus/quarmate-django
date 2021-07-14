from django.shortcuts import render

from rest_framework import viewsets

from .serializers import *
from .models import *


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('person_id')
    serializer_class = PersonSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all().order_by('guest_id')
    serializer_class = GuestSerializer

class HousemateViewSet(viewsets.ModelViewSet):
    queryset = Housemate.objects.all().order_by('housemate_id')
    serializer_class = HousemateSerializer

class ResidenceViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all().order_by('residence_id')
    serializer_class = ResidenceSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('room_id')
    serializer_class = RoomSerializer

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all().order_by('visit_id')
    serializer_class = VisitSerializer