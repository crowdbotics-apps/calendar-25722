from rest_framework import authentication
from task_profile.models import CustomerProfile, InviteCode, Notification, TaskerProfile
from .serializers import (
    CustomerProfileSerializer,
    InviteCodeSerializer,
    NotificationSerializer,
    TaskerProfileSerializer,
)
from rest_framework import viewsets


class InviteCodeViewSet(viewsets.ModelViewSet):
    serializer_class = InviteCodeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = InviteCode.objects.all()


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Notification.objects.all()


class TaskerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerProfile.objects.all()


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerProfile.objects.all()
