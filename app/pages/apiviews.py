from rest_framework import viewsets
from app.pages.models import ContentPiece, Page
from app.pages.serializers import CPiecePolymorphicSerializer, PageSerializer


class CPieceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContentPiece.objects.all()
    serializer_class = CPiecePolymorphicSerializer


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
