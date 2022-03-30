from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from app.pages.models import TextPiece, AudioPiece, VideoPiece, Page


class BaseCPieceSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('polymorphic_ctype',)
        abstract = True


class TextPieceSerializer(BaseCPieceSerializer):
    class Meta(BaseCPieceSerializer.Meta):
        model = TextPiece


class AudioPieceSerializer(BaseCPieceSerializer):
    class Meta(BaseCPieceSerializer.Meta):
        model = AudioPiece


class VideoPieceSerializer(BaseCPieceSerializer):
    class Meta(BaseCPieceSerializer.Meta):
        model = VideoPiece


class CPiecePolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        TextPiece: TextPieceSerializer,
        AudioPiece: AudioPieceSerializer,
        VideoPiece: VideoPieceSerializer,
    }


class PageSerializer(serializers.ModelSerializer):
    pieces = CPiecePolymorphicSerializer(many=True)

    class Meta:
        model = Page
        fields = '__all__'
