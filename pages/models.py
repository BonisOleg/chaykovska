from django.db import models
from cloudinary.models import CloudinaryField
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _


class MosaicCell(models.Model):
    """Homepage mosaic cell with 3 rotating images."""
    
    SIZE_CHOICES = [
        ('half', _('Half Width (1 col)')),
        ('full_width', _('Full Width (2 cols)')),
        ('double_height', _('Double Height (2 rows)')),
    ]
    
    position = models.PositiveIntegerField(
        unique=True,
        help_text='Cell position 1-12 (6 rows x 2 cols)'
    )
    size_type = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        default='half'
    )
    
    image_1 = CloudinaryField(
        'image_1',
        help_text='First image to rotate'
    )
    image_2 = CloudinaryField(
        'image_2',
        help_text='Second image to rotate'
    )
    image_3 = CloudinaryField(
        'image_3',
        help_text='Third image to rotate'
    )
    
    link = models.URLField(
        blank=True,
        null=True,
        help_text='Optional: Where cell click navigates'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Show or hide this cell'
    )
    
    class Meta:
        verbose_name = 'Mosaic Cell'
        verbose_name_plural = 'Mosaic Cells'
        ordering = ['position']
    
    def __str__(self):
        return f'Cell {self.position} ({self.get_size_type_display()})'


class AboutSection(models.Model):
    """About page sections (Brand, Fabrics, Production)."""
    
    SECTION_CHOICES = [
        ('brand', _('Brand')),
        ('fabrics', _('Fabrics')),
        ('production', _('Production')),
    ]
    
    section_type = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        unique=True
    )
    title = models.CharField(
        max_length=200,
        help_text='Section title (translatable)'
    )
    content = models.TextField(
        help_text='Section content (translatable)'
    )
    image = CloudinaryField(
        'image',
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'
    
    def __str__(self):
        return self.get_section_type_display()


class ContactInfo(SingletonModel):
    """Contacts page information (singleton)."""
    
    address = models.TextField(
        help_text='Showroom address (translatable)'
    )
    phone = models.CharField(
        max_length=20,
        help_text='Contact phone number'
    )
    email = models.EmailField(
        help_text='Contact email'
    )
    working_hours = models.TextField(
        help_text='Working hours (translatable)'
    )
    map_url = models.URLField(
        blank=True,
        null=True,
        help_text='Google Maps embed URL'
    )
    
    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'
    
    def __str__(self):
        return 'Contact Information'
