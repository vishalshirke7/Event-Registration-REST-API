from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Event, InvitationsSent


class CreateEventSerializer(serializers.Serializer):
    title = serializers.CharField()
    venue = serializers.CharField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    private = serializers.BooleanField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)


class ListOfEvents(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ('organizer', 'id',)


class InvitationsSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField()

    class Meta:
        model = InvitationsSent
        exclude = ('organizer', 'accepted')

    # def create(self, validated_data):
    #     return Event.objects.create(**validated_data)


class ListOfInvitedUsers(serializers.ModelSerializer):

    class Meta:
        model = InvitationsSent
        exclude = ('organizer', 'id',)


class PublicEventsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ('organizer', 'id', 'private')


class RegisterOrUnregisterForEvent(serializers.ModelSerializer):

    class Meta:
        model = InvitationsSent
        exclude = ('organizer', 'id', 'email')