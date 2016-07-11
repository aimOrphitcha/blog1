from django.contrib import admin
from blogpost.models import Blogpost


class BlogpostAdmin(admin.ModelAdmin):
    fields = ('title', 'content')
    list_display = ('title', 'pub_date',)
admin.site.register(Blogpost, BlogpostAdmin)
