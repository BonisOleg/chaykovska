from django.views.generic import ListView, TemplateView
from .models import MosaicCell, AboutSection, ContactInfo


class HomeView(ListView):
    model = MosaicCell
    template_name = 'pages/home.html'
    context_object_name = 'mosaic_cells'
    
    def get_queryset(self):
        return MosaicCell.objects.filter(is_active=True).order_by('position')


class AboutView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = AboutSection.objects.all()
        return context


class ContactsView(TemplateView):
    template_name = 'pages/contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['contact_info'] = ContactInfo.objects.get()
        except ContactInfo.DoesNotExist:
            context['contact_info'] = None
        return context
