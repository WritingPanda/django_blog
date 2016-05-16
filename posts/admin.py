from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated_on"]
    list_display_links = ["title", "timestamp", "updated_on"]
    list_filter = ["updated_on", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
