from django.shortcuts import render
from core.models import BookJournalBase, Book, Journal
from core.serializers import BookJournalBaseSerializer, BookSerializer, JournalSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action


# Create your views here.

class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.all()


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Journal.objects.all()


