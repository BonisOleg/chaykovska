from django.urls import path
from django.views.i18n import set_language
from . import views

app_name = 'core'

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
]
