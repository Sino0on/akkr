from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ApplicationForm
from .models import *


class HomeTemplateView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['news'] = News.objects.all()[:3]
        context['sponsors'] = Sponsor.objects.all()
        context['contacts'] = Contacts.load()
        context['pages'] = Page.objects.all()
        context['more_pages'] = MorePage.objects.all().order_by('created_at')
        context['members'] = TeamMember.objects.all()
        context['category_news'] = NewsCategory.objects.all()
        context['category_project'] = ProjectCategory.objects.all()
        context['category_publish'] = PublicationCategory.objects.all()
        return context


class ProjectDetailView(generic.DetailView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['news'] = News.objects.all()[:3]
        context['sponsors'] = Sponsor.objects.all()
        context['contacts'] = Contacts.load()
        context['pages'] = Page.objects.all()
        context['members'] = TeamMember.objects.all()
        context['category_news'] = NewsCategory.objects.all()
        context['category_project'] = ProjectCategory.objects.all()
        context['category_publish'] = PublicationCategory.objects.all()
        context['more_pages'] = MorePage.objects.all()
        return context



class NewsDetailView(generic.DetailView):
    model = News
    queryset = News.objects.all()
    template_name = 'blog-details.html'
    context_object_name = 'news'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = News.objects.filter(slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.load()
        context['projects'] = Project.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['contacts'] = Contacts.load()
        context['pages'] = Page.objects.all()

        return context


class AboutUsView(generic.TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.load()
        context['contacts'] = Contacts.load()
        context['pages'] = Page.objects.all()
        context['members'] = TeamMember.objects.all()
        context['projects'] = Project.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['gallery'] = GalleryImage.objects.all()
        return context


class NewsListView(generic.ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'news.html'
    paginate_by = 10
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsCategory.objects.all()
        context['contacts'] = Contacts.load()
        context['more_pages'] = MorePage.objects.all()
        context['projects'] = Project.objects.all()
        context['pages'] = Page.objects.all()
        context['members'] = TeamMember.objects.all()
        return context


class ProjectsListView(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'projects.html'
    paginate_by = 10
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['projects'] = Project.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['pages'] = Page.objects.all()
        context['contacts'] = Contacts.load()
        context['members'] = TeamMember.objects.all()
        return context


class PageDetailView(generic.DetailView):
    model = Page
    queryset = Page.objects.all()
    template_name = 'blank-page.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['projects'] = Project.objects.all()
        context['pages'] = Page.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['contacts'] = Contacts.load()
        context['members'] = TeamMember.objects.all()
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Page.objects.filter(slug=slug)
        return queryset


class MorePageDetailView(generic.DetailView):
    model = MorePage
    queryset = MorePage.objects.all()
    template_name = 'blank-page.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['projects'] = Project.objects.all()
        context['pages'] = Page.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['contacts'] = Contacts.load()
        context['members'] = TeamMember.objects.all()
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = MorePage.objects.filter(slug=slug)
        return queryset


class ApplicationCreateView(generic.CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['projects'] = Project.objects.all()
        context['pages'] = Page.objects.all()
        context['more_pages'] = MorePage.objects.all()
        context['contacts'] = Contacts.load()
        context['members'] = TeamMember.objects.all()
        return context
