from django.contrib import admin

from .models import Bd, Rubric, Novelty

class BdAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Novelty)
