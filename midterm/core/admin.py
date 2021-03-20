from django.contrib import admin
from core.models import BookJournalBase, Book, Journal
# Register your models here.

admin.site.register(BookJournalBase)
admin.site.register(Book)
admin.site.register(Journal)
