from django.contrib import admin
from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'datetome_created', ]


admin.site.register(Comment, CommentAdmin)
admin.site.register(Book)
