from django.contrib import admin

from .models import Cat, Breed, Rating

admin.site.register(Cat)
admin.site.register(Breed)
admin.site.register(Rating)
