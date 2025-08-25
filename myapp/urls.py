from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    path('more-page/<slug:slug>/', MorePageDetailView.as_view(), name='morepage_detail'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('news/', NewsListView.as_view(), name='news'),
    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('publish/<int:pk>/', PublishListView.as_view(), name='category_publish_detail'),
    path('application/', ApplicationCreateView.as_view(), name='application'),
]
