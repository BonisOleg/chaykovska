from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import MosaicCell, AboutSection, ContactInfo


@admin.register(MosaicCell)
class MosaicCellAdmin(admin.ModelAdmin):
    list_display = ('position', 'size_type', 'is_active')
    list_filter = ('size_type', 'is_active')
    list_editable = ('is_active',)
    ordering = ['position']
    
    fieldsets = (
        ('Position & Size', {
            'fields': ('position', 'size_type', 'is_active')
        }),
        ('Images (3 rotating)', {
            'fields': ('image_1', 'image_2', 'image_3')
        }),
        ('Slide Direction', {
            'fields': ('slide_direction',),
            'classes': ('collapse',),
            'description': 'Direction the new image enters from on hover (push transition)'
        }),
        ('Link (optional)', {
            'fields': ('link',),
            'classes': ('collapse',)
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'title')
    list_filter = ('section_type',)
    
    fieldsets = (
        ('Section Type', {
            'fields': ('section_type',)
        }),
        ('Контент (UK)', {
            'fields': ('title_uk', 'content_uk', 'image')
        }),
        ('Content (EN)', {
            'fields': ('title_en', 'content_en')
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Address & Contact', {
            'fields': ('address_uk', 'address_en', 'phone', 'email')
        }),
        ('Hours & Map', {
            'fields': ('working_hours_uk', 'working_hours_en', 'map_url')
        }),
    )
