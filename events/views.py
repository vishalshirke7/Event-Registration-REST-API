from functools import partial
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateEventSerializer, ListOfEvents, InvitationsSerializer, ListOfInvitedUsers\
                         , PublicEventsListSerializer, RegisterOrUnregisterForEvent, LimitAttendeesSerializer\
                         , ListOfIndividuallyCreatedEventsSerializer
from .models import Event, InvitationsSent
from userregistration.models import User


class CustomPermissionsForUser(permissions.BasePermission):

    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if 'user_id' in request.session.keys():
            return request.method in self.allowed_methods


class CreateEvent(APIView):
    """
    Create an Event or List all Events
    """
    serializer_class = CreateEventSerializer
    permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = ListOfEvents(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CreateEventSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.get(pk=request.session['user_id'])
            serializer.save(organizer=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InviteUsers(APIView):
    """
    Invite other users for an event created by you.
    """
    serializer_class = InvitationsSerializer
    permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def get(self, request, format=None):
        user = User.objects.get(pk=request.session['user_id'])
        invitations = InvitationsSent.objects.filter(organizer=user)
        serializer = ListOfInvitedUsers(invitations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationsSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.get(pk=request.session['user_id'])
            event = Event.objects.get(pk=request.data['event'])
            serializer.save(organizer=user, event=event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewPublicEvents(APIView):
    """

    View all public events
    """
    # serializer_class = PublicEventsListSerializer
    permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD']),)

    def get(self, request, format=None):

        events = Event.objects.filter(private=False)
        serializer = PublicEventsListSerializer(events, many=True)
        return Response(serializer.data)


class RegisterUnregisterForEvent(APIView):
    """
    Register or Unregister (i.e accept/reject an invitation for a event organized by other users)4
    This also checks for previously registered event and if it is overlapping then it does not register for event
    """
    serializer_class = RegisterOrUnregisterForEvent
    permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def get(self, request, format=None):
        user = User.objects.get(pk=request.session['user_id'])
        invitations = InvitationsSent.objects.filter(email=user.email)
        serializer = RegisterOrUnregisterForEvent(invitations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = User.objects.get(pk=request.session['user_id'])
        event = Event.objects.get(title=request.data.get('title'))
        invitation = InvitationsSent.objects.get(email=user.email, event=event)
        serializer = RegisterOrUnregisterForEvent(invitation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LimitNumberOfAttendees(APIView):
    """
    Limit number of attendees at anytime by changing the number of attendees
    """

    serializer_class = LimitAttendeesSerializer
    permission_classes = (partial(CustomPermissionsForUser, ['GET', 'HEAD', 'POST']),)

    def get(self, request, format=None):
        user = User.objects.get(pk=request.session['user_id'])
        events = Event.objects.filter(organizer=user)
        serializer = ListOfIndividuallyCreatedEventsSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = User.objects.get(pk=request.session['user_id'])
        event = Event.objects.get(pk=request.data.get('id'))
        serializer = LimitAttendeesSerializer(event, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

