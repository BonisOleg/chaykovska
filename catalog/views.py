from django.views.generic import ListView, DetailView
from .models import Product, Category


class CatalogView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'
    paginate_by = 30
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True).select_related('category').prefetch_related('images')
        
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['selected_category'] = Category.objects.get(slug=category_slug)
        
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    
    def get_queryset(self):
        return Product.objects.filter(is_available=True).prefetch_related('images')
