from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ('product', 'quantity', 'price')
    readonly_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Customer Info', {
            'fields': ('first_name', 'last_name', 'phone', 'email')
        }),
        ('Delivery', {
            'fields': ('address',)
        }),
        ('Order Status', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('order__created_at',)
    readonly_fields = ('order', 'product', 'price')
