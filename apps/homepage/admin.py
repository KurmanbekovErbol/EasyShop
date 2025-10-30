from django.contrib import admin
from apps.homepage.models import Content, Homepage, Sections, Statistics, HeaderFooter, Partner, Brand
from modeltranslation.admin import TranslationAdmin
from apps.homepage.translation import *

class HomepageAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'content_ru')
        }),
        ('Английская версия', {
            'fields': ('title_en', 'content_en')
        }),
        ('Китайская версия', {
            'fields': ('title_zh_hans', 'content_zh_hans')
        }),
        ('Файл', {
            'fields': ('file',)
        }),
    )

admin.site.register(Homepage, HomepageAdmin)

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('users_count', 'bought_products_count', 'total_products_count')


class PartnerInline(admin.TabularInline):
    model = Partner
    extra = 1
    verbose_name = "Партнер"
    verbose_name_plural = "Партнеры"


class BrandInline(admin.TabularInline):
    model = Brand
    extra = 1
    verbose_name = "Бренд"
    verbose_name_plural = "Бренды"


@admin.register(HeaderFooter)
class HeaderFooterAdmin(admin.ModelAdmin):
    list_display = ("title", "bottom_text", "instagram", "telagram", "vk")
    search_fields = ("title", "bottom_text")
    inlines = [PartnerInline, BrandInline]
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'bottom_text_ru')
        }),
        ('Английская версия', {
            'fields': ('title_en', 'bottom_text_en')
        }),
        ('Китайская версия', {
            'fields': ('title_zh_hans', 'bottom_text_zh_hans')
        }),
        ("Логотипы", {
            "fields": ("top_logo", "bottom_logo")
        }),
        ("Социальные сети", {
            "fields": ("instagram", "telagram", "vk")
        }),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "footer")
    search_fields = ("name",)
    list_filter = ("footer",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "footer")
    search_fields = ("name",)
    list_filter = ("footer",)


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1
    fields = ('title', 'description', 'image')
    show_change_link = True


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [ContentInline]
    fieldsets = (
        ('Русская версия', {
            'fields': ('name_ru', 'description_ru')
        }),
        ('Английская версия', {
            'fields': ('name_en', 'description_en')
        }),
        ('Китайская версия', {
            'fields': ('name_zh_hans', 'description_zh_hans')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'section')
    search_fields = ('title', 'description')
    list_filter = ('section',)
    fieldsets = (
        ('Русская версия', {
            'fields': ('title_ru', 'description_ru')
        }),
        ('Английская версия', {
            'fields': ('title_en', 'description_en')
        }),
        ('Китайская версия', {
            'fields': ('title_zh_hans', 'description_zh_hans')
        }),
        ('Общий', {
            'fields': ('section', 'image')
        }),
    )