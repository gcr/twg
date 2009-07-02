from django.contrib import admin
from twg.stories.models import Story, Fragment

class FragmentInline(admin.TabularInline):
    model = Fragment
    
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update_date', 'fulltext')
    list_filter = ('last_update_date',)
    search_fields = ('name',)
    inlines = [FragmentInline]

admin.site.register(Story, StoryAdmin)


