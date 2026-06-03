from django.contrib import admin
from .models import APP
# Register your models here.

@admin.register(APP)
class HashtagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'likes', 'logo_app', 'data_created',)
    search_fields = ('name', )
    