from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from .models import User
from .serializers import UserSerializer
import json
from rest_framework.response import Response
from rest_framework import status

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        username = self.request.query_params.get('username')
        return User.objects.get(username=username)


class EventUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        events = request.data.get('events')
        username = request.data.get('username')
        user = User.objects.get(username=username)
        user.events = json.dumps(events)
        user.save()

        return Response(status=status.HTTP_200_OK)