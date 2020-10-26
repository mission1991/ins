from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['updated', 'created', 'author']
    search_fields = ['text', 'created', 'updated', 'author__username']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
