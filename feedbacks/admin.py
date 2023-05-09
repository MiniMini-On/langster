from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class BookmarkAdmin(admin.ModelAdmin):  
    list_display = ('id', 'title', 'content', 'is_checked', 'created_at', 'updated_at',)
    list_filter = ('title', 'is_checked',)

