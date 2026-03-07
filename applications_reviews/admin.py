from django.contrib import admin
from .models import APPReview


@admin.register(APPReview)
class APPReviewAdmin(admin.ModelAdmin):
    list_display = ('app', 'stars', )
    list_filter = ('app',)