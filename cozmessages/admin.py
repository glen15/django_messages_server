from django.contrib import admin
from .models import Cozmessage, Submit

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

@admin.register(Submit)
class SubmitAdmin(admin.ModelAdmin):

    list_display = ("name", "githubId", "getMethod", "postMethod", "deleteMethod")
    list_filter = ("name", "githubId",)
    search_fields = ("name", "githubId",)