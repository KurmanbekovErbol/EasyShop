from modeltranslation.translator import register, TranslationOptions
from apps.homepage.models import Homepage, HeaderFooter, Content, Sections


@register(Homepage)
class HomepageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(HeaderFooter)
class HeaderFooterTranslationOptions(TranslationOptions):
    fields = ('title', 'bottom_text',)

@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(Sections)
class SectionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)