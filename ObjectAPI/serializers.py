from rest_framework import serializers

from .models import *

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('person_id', 'person_name', 'date', 'status')

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ('person_id', 'person_name', 'date', 'status', 'guest_id')

class HousemateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Housemate
        fields = ('person_id', 'person_name', 'date', 'status', 'housemate_id', 'email', 'guests')

class ResidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residence
        fields = ('residence_id', 'residence_name', 'address', 'rooms', 'housemates', 'visits')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('room_id', 'room_name')

class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = ('visit_id', 'housemate', 'rooms', 'guests')
