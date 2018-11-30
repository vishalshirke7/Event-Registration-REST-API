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


class RegisterOrUnregisterForEvent(serializers.Serializer):

    title = serializers.CharField()
    accepted = serializers.BooleanField()

    def update(self, instance, validated_data):
        instance.accepted = validated_data.get('accepted', instance.accepted)
        instance.save()
        return instance


class LimitAttendeesSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    max_attendees = serializers.IntegerField()

    def update(self, instance, validated_data):
        # instance.id = validated_data.get('event_id', instance.id)
        instance.max_attendees = validated_data.get('max_attendees', instance.max_attendees)
        instance.save()
        return instance


class ListOfIndividuallyCreatedEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'



