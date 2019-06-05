from django.contrib import admin
from blog.models import post

class postAdmin(admin.ModelAdmin):
    list_display = ["title","author","slug","publish","body","created","updated","status"]
    list_filter = ["status","author","created","publish"]
    prepopulated_fields = {"slug":("title",)}
    search_fields = ("title","body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["status","publish"]


admin.site.register(post,postAdmin)
