from django.contrib import admin
from .models import Cozmessage

@admin.register(Cozmessage)
class CozmessageAdmin(admin.ModelAdmin):
    
    list_display = (
        "username",
        "text",
        "roomname"
    )

    list_filter = (
        "username",
    )

    search_fields = ("username",)

