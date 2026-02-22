from django.contrib import admin
from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'position')
    ordering = ['position']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name_uk',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'price_eur', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    list_editable = ('is_available',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Назва та опис (UK)', {
            'fields': ('name_uk', 'description_uk')
        }),
        ('Name & description (EN)', {
            'fields': ('name_en', 'description_en')
        }),
        ('Product Info', {
            'fields': ('slug', 'category', 'price', 'price_eur', 'is_available')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
