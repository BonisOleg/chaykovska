from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """Product category."""
    
    name = models.CharField(
        max_length=200,
        help_text='Category name (translatable)'
    )
    slug = models.SlugField(
        unique=True,
        help_text='URL slug'
    )
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Fashion product."""
    
    name = models.CharField(
        max_length=200,
        help_text='Product name (translatable)'
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text='URL slug (auto-generated from name)'
    )
    description = models.TextField(
        help_text='Product description (translatable)'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Price in UAH'
    )
    price_eur = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Price in EUR (European market)'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    is_available = models.BooleanField(
        default=True,
        help_text='Is product available for purchase'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """Product image (Cloudinary)."""
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = CloudinaryField(
        'image',
        help_text='Product image'
    )
    position = models.PositiveIntegerField(
        default=0,
        help_text='Display order'
    )
    
    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ['product', 'position']
    
    def __str__(self):
        return f'{self.product.name} - Image {self.position}'
