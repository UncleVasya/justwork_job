from django.urls import path
from app.pages.views import ContentPieceAutocomplete


urlpatterns = [
    path(r'cpiece-autocomplete', ContentPieceAutocomplete.as_view(), name='cpiece-autocomplete'),
]