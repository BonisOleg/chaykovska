from django.db import models
from solo.models import SingletonModel
from cloudinary.models import CloudinaryField


class SiteSettings(SingletonModel):
    """Global site settings (singleton)."""
    
    logo = CloudinaryField(
        'logo',
        null=True,
        blank=True,
        help_text='Logo for header (CHAYKOVSKA)'
    )
    phone_number = models.CharField(
        max_length=20,
        default='+380',
        help_text='Primary phone number'
    )
    email = models.EmailField(
        default='info@chaykovska.com',
        help_text='Contact email'
    )
    
    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'
    
    def __str__(self):
        return 'Site Settings'
