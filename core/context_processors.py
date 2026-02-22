from .models import SiteSettings


def site_settings(request):
    """Inject site settings into template context."""
    try:
        settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        settings = None
    
    return {
        'site_settings': settings,
    }


def cart_context(request):
    """Inject cart count into template context."""
    from cart.utils import SessionCart
    
    cart = SessionCart(request.session)
    return {
        'cart_count': cart.get_count(),
    }
