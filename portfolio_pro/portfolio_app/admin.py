from django.contrib import admin
from .models import Contact

@admin.register(Contact)   # <-- yaha decorator lagana better hai
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")  # <-- 'creted_at' ki spelling galat thi
    search_fields = ("name", "email", "message")
