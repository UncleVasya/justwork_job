from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, \
    StackedPolymorphicInline, PolymorphicInlineSupportMixin
from app.pages.models import ContentPiece, TextPiece, AudioPiece, VideoPiece, Page


class BaseContentPiece(PolymorphicChildModelAdmin):
    base_model = ContentPiece


class TextPieceAdmin(BaseContentPiece):
    base_model = TextPiece


class AudioPieceAdmin(BaseContentPiece):
    base_model = AudioPiece


class VideoPieceAdmin(BaseContentPiece):
    base_model = VideoPiece


class ContentPieceAdmin(PolymorphicParentModelAdmin):
    base_model = ContentPiece
    child_models = (TextPiece, AudioPiece, VideoPiece)


class ContentPieceInline(StackedPolymorphicInline):
    class TextAdminInline(StackedPolymorphicInline.Child):
        model = TextPiece

    class AudioAdminInline(StackedPolymorphicInline.Child):
        model = AudioPiece

    class VideoAdminInline(StackedPolymorphicInline.Child):
        model = VideoPiece

    model = Page.pieces.through
    child_inlines = (TextAdminInline, AudioAdminInline, VideoAdminInline)


class PageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (ContentPieceInline,)


admin.site.register(TextPiece, TextPieceAdmin)
admin.site.register(AudioPiece, AudioPieceAdmin)
admin.site.register(VideoPiece, VideoPieceAdmin)
admin.site.register(ContentPiece, ContentPieceAdmin)

admin.site.register(Page, PageAdmin)