from django.contrib import admin
from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'datetime_created', 'recommend', 'is_active', ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Book)
