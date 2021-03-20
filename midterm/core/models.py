from datetime import datetime

from django.db import models

from utils.constants import TYPES

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=TYPES)
    publisher = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'