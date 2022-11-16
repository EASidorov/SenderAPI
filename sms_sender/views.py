from django.shortcuts import render

import rest_framework.views
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *
from .stats import show_stats


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class StatsViewSet(rest_framework.views.APIView):
    @staticmethod
    def get(request):
        return Response(show_stats())
