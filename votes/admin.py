from django.contrib import admin
from .models import Vote

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'app', 'createdAt', 'updateAt']
    filter_horizontal = ['users']
    