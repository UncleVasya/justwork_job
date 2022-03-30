from rest_framework import viewsets
from app.pages.models import ContentPiece, Page
from app.pages.serializers import CPiecePolymorphicSerializer, PageSerializer
from app.pages.tasks import update_page_counters


class CPieceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContentPiece.objects.all()
    serializer_class = CPiecePolymorphicSerializer


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, pk=None):
        update_page_counters.delay(pk)
        return super(PageViewSet, self).retrieve(request, pk)
