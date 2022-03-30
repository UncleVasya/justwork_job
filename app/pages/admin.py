from dal import autocomplete
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


class AudioPieceAdmin(BaseContentPiece):
    base_model = AudioPiece


class VideoPieceAdmin(BaseContentPiece):
    base_model = VideoPiece


class ContentPieceAdmin(PolymorphicParentModelAdmin):
    base_model = ContentPiece
    child_models = (TextPiece, AudioPiece, VideoPiece)
    search_fields = ['title__istartswith']


class ContentPieceInlineForm(forms.ModelForm):
    piece = forms.ModelChoiceField(
        queryset=ContentPiece.objects.all(),
        widget=autocomplete.ModelSelect2(url='pages:cpiece-autocomplete')
    )

    class Meta:
        model = ContentPiece
        fields = '__all__'


class ContentPieceInline(admin.StackedInline):
    class TextAdminInline(StackedPolymorphicInline.Child):
        model = TextPiece

    class AudioAdminInline(StackedPolymorphicInline.Child):
        model = AudioPiece

    class VideoAdminInline(StackedPolymorphicInline.Child):
        model = VideoPiece

    model = Page.pieces.through
    form = ContentPieceInlineForm
    child_inlines = (TextAdminInline, AudioAdminInline, VideoAdminInline)


class PageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    model = Page
    search_fields = ['title__istartswith']
    inlines = (ContentPieceInline,)


admin.site.register(TextPiece, TextPieceAdmin)
admin.site.register(AudioPiece, AudioPieceAdmin)
admin.site.register(VideoPiece, VideoPieceAdmin)
admin.site.register(ContentPiece, ContentPieceAdmin)

admin.site.register(Page, PageAdmin)
