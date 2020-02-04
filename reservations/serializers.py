from rest_framework import serializers
from reservations.models import Reservation,Avail, Table, Timestart


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['table',
                'customer',
                'product',
                'timestart',
                'duration',
                'date']

class AvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avail
        fields = ['name',
                'reservation',
                'date']

class TimestartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestart
        fields = ['name']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['pk','name']


        