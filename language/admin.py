from django.contrib import admin
from .models import Suggestion

@admin.register(Suggestion)
class BookmarkAdmin(admin.ModelAdmin):  
    list_display = ('id', 'content', 'is_checked', 'created_at', 'updated_at',)
    list_filter = ('is_checked',)
