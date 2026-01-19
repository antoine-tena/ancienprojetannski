from django.contrib import admin
from .models import HeaderConfig, HeaderButton, Page


class HeaderButtonInline(admin.TabularInline):
    model = HeaderButton
    extra = 1


@admin.register(HeaderConfig)
class HeaderConfigAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo_text', 'show_login_button', 'background_color', 'text_color']
    inlines = [HeaderButtonInline]


@admin.register(HeaderButton)
class HeaderButtonAdmin(admin.ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_visible', 'header_config']
    list_filter = ['is_visible', 'header_config']
    ordering = ['order']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent', 'order', 'is_visible']
    list_filter = ['is_visible', 'parent']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
