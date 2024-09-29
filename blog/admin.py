from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class CommentTabular(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentTabular,
    ]
    list_display = ['title', 'status', 'publish', 'created']
    list_filter = ['created', 'publish', 'status']
    search_fields = ['author', 'title', 'body']
    date_hierarchy = "publish"
    ordering = ['-status', '-publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created', 'updated', "is_active"]
    list_filter = ['created', 'updated', 'is_active']
    search_fields = ['body', 'author_email']
    date_hierarchy = 'created'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
