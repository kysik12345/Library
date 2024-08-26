from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('lastname', 'name')

#     def author_name(self, obj):
#         return obj.author.name
