from django.contrib import admin
from .models import Hashtags
# Register your models here.

@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', )
    