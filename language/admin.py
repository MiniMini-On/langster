from django.contrib import admin
from .models import Suggestion, TestNum

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):  
    list_display = ('id', 'content', 'is_checked', 'created_at', 'updated_at',)
    list_filter = ('is_checked',)
    
@admin.register(TestNum)
class TestNumAdmin(admin.ModelAdmin):  
    list_display = ('id', 'number', 'created_at', 'updated_at',)
