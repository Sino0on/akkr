from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'mini_title', 'content')


@register(Document)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProjectCategory)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Project)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(NewsCategory)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(PublicationCategory)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Publication)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutUs)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'description2', 'description3', 'title2')


@register(Page)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(MorePage)
class CategoryVacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'mini_title', 'description')


@register(PageImage)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(GalleryImage)
class IndustryTranslationOptions(TranslationOptions):
    fields = ('title', )

