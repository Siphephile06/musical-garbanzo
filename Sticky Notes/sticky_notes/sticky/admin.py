# sticky/admin.py 
from django.contrib import admin 
from .models import StickyNote, Topic

# StickyNote model 
admin.site.register(StickyNote) 
# Topic model 
admin.site.register(Topic) 
