from dal import autocomplete
from app.pages.models import ContentPiece


class ContentPieceAutocomplete(autocomplete.Select2QuerySetView):
    queryset = ContentPiece.objects.order_by('title')
    model_field_name = 'title'
