from django.contrib import admin
from .models import *

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'email_address')
    search_fields = ('title', 'subtitle')
    list_filter = ('title',)
    ordering = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'bio')

@admin.register(Skilled)
class SkilledAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'bio')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'proficiency')
    list_filter = ('proficiency',)
    search_fields = ('skill_name',)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('project_name',)
    search_fields = ('project_name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')
