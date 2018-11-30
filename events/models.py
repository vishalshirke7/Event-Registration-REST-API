from django.db import models
import userregistration
from userregistration.models import User


class Event(models.Model):

    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    venue = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    private = models.BooleanField(default=False)
    max_attendees = models.IntegerField(default=50)


class InvitationsSent(models.Model):

    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email = models.EmailField()
    accepted = models.BooleanField(default=False)
