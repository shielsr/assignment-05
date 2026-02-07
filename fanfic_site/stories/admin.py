from django.contrib import admin
from .models import Story, Chapter, Genre


# Inline editing of chapters inside a story
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1  # One empty row for new chapters


# Register Story with chapter inline only
@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ("title", "author", "summary", "genre", "date_published")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
