from django.contrib import admin
from .models import (
    Sponsor, TeamMember, Document, ProjectCategory, Project,
    NewsCategory, News, PublicationCategory, Publication,
    ContactMessage, Subscription, Contacts, AboutUs, Page, MorePage, PageImage, MorePageImage, Application,
    GalleryImage, FileCategoryPage
)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('completed',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PublicationCategory)
class PublicationCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ImagePageInline(admin.StackedInline):
    model = PageImage
    extra = 1

class ImageMorePageInline(admin.StackedInline):
    model = MorePageImage
    extra = 1

@admin.register(Page)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImagePageInline]

# admin.py
from django.contrib import admin
from .models import ContactMessage

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('name', 'email', 'message')


@admin.register(MorePage)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageMorePageInline]

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)


admin.site.register(Contacts)
admin.site.register(AboutUs)
admin.site.register(GalleryImage)
admin.site.register(FileCategoryPage)
# admin.site.register(MorePage)


