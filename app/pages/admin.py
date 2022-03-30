from adminsortable2.admin import SortableInlineAdminMixin
from dal import autocomplete
import djhacker
from django import forms
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, \
                              StackedPolymorphicInline, PolymorphicInlineSupportMixin
from app.pages.models import ContentPiece, TextPiece, AudioPiece, VideoPiece, Page


class BaseContentPiece(PolymorphicChildModelAdmin):
    base_model = ContentPiece
    search_fields = ['title__istartswith']


class TextPieceAdmin(BaseContentPiece):
    base_model = TextPiece
    show_in_index = True


class AudioPieceAdmin(BaseContentPiece):
    base_model = AudioPiece
    show_in_index = True


class VideoPieceAdmin(BaseContentPiece):
    base_model = VideoPiece
    show_in_index = True


class ContentPieceAdmin(PolymorphicParentModelAdmin):
    base_model = ContentPiece
    child_models = (TextPiece, AudioPiece, VideoPiece)
    search_fields = ['title__istartswith']

    def get_model_perms(self, request):
        return {}  # hide this from admin panel


djhacker.formfield(
    Page.pieces.through.piece,
    forms.ModelChoiceField,
    queryset=ContentPiece.objects.all(),
    widget=autocomplete.ModelSelect2(url='pages:cpiece-autocomplete')
)


class ContentPieceInline(SortableInlineAdminMixin, admin.StackedInline):
    class TextAdminInline(StackedPolymorphicInline.Child):
        model = TextPiece

    class AudioAdminInline(StackedPolymorphicInline.Child):
        model = AudioPiece

    class VideoAdminInline(StackedPolymorphicInline.Child):
        model = VideoPiece

    model = Page.pieces.through
    child_inlines = (TextAdminInline, AudioAdminInline, VideoAdminInline)


class PageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    model = Page
    search_fields = ['title__istartswith']
    inlines = (ContentPieceInline,)


admin.site.register(ContentPiece, ContentPieceAdmin)
admin.site.register(TextPiece, TextPieceAdmin)
admin.site.register(AudioPiece, AudioPieceAdmin)
admin.site.register(VideoPiece, VideoPieceAdmin)

admin.site.register(Page, PageAdmin)
