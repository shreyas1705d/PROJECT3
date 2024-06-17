from django.contrib import admin
from .models import *

admin.site.register(Customer)
# Define a custom admin class for Feedback model
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_quality', 'product_quality', 'delivery_speed', 'overall_experience', 'created_at')
    list_filter = ('service_quality', 'product_quality', 'delivery_speed', 'overall_experience', 'created_at')
    search_fields = ('name', 'email', 'additional_comments')
    readonly_fields = ('created_at',)  # Optional: Make created_at read-only in admin

    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
        ('Feedback Details', {
            'fields': ('service_quality', 'product_quality', 'delivery_speed', 'overall_experience', 'additional_comments')
        }),
        ('Date Information', {
            'fields': ('created_at',)
        }),
    )

    # Optionally define inlines if needed



# Register your models here.
