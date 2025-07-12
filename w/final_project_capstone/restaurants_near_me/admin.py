from django.contrib import admin
from .models import User, Restaurant, Review, Like

# Register your models here.
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Like)
