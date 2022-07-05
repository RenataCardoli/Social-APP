from datetime import date
from django.contrib import admin
from .models import Post, Contact, Comments

class PostModel(admin.ModelAdmin):
        list_display = ('title', 'date_created')
admin.site.register(Post , PostModel)

admin.site.register(Contact)
admin.site.register(Comments)

