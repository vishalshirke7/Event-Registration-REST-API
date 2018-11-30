from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [

    path('create-event/', views.CreateEvent.as_view(), name='create_event'),
    path('invite-users/', views.InviteUsers.as_view(), name='invite_user'),
    path('view-all-events/', views.ViewPublicEvents.as_view(), name='view-events'),
    path('register-unregister/', views.RegisterUnregisterForEvent.as_view(), name='register-unregister'),
    path('limit-attendees/', views.LimitNumberOfAttendees.as_view(), name='limit-attendees'),
]