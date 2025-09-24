from django.contrib import admin
from .models import Project, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)  # nice UI for ManyToMany

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

