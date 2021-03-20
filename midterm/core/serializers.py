from core.models import BookJournalBase, Book, Journal
from rest_framework import serializers


class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

