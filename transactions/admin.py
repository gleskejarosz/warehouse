from django.contrib import admin

from transactions.models import TransactionType, TransactionArchive

admin.site.register(TransactionType)
admin.site.register(TransactionArchive)
