from django.db import models

class Suggestion(models.Model):   
    
    content = models.CharField(max_length=50, blank=False, null=False)
    is_bad = models.BooleanField(null=False, blank=False)
    is_checked = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
class TestNum(models.Model):   
    
    number = models.PositiveIntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    

  
