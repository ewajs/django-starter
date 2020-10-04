from django.contrib import admin

from .models import Comment

# Add my comment model to the Django Admin page
admin.site.register(Comment)
