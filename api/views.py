from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer, DocsSerializer, TalkSerializer
from .models import Docs, Talk


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


# test なんとかできたーw
class DocsListView(generics.ListAPIView):
    queryset = Docs.objects.all().order_by('created_at')
    serializer_class = DocsSerializer
    permission_classes = (AllowAny,)


class DocsRetrieveView(generics.RetrieveAPIView):
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'


class TalkListView(generics.ListAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    permission_classes = (AllowAny,)


class TalkRetrieveView(generics.RetrieveAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'



