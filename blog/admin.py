from django.contrib import admin
from .models import Blog, Comment, Author, Biography

class BlogAdmin(admin.ModelAdmin):
	list_display = ('name', 'author')
admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('blog', 'date', 'author')
admin.site.register(Comment, CommentAdmin)

class BiographyAdmin(admin.ModelAdmin):
	list_display = ('blogger', 'content')
admin.site.register(Biography, BiographyAdmin)
