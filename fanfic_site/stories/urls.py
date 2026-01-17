from django.urls import path
from .views import StoryListView, StoryDetailView
from .views import (
    StoryListView,
    StoryDetailView,
    StoryCreateView,
    StoryUpdateView,
    StoryDeleteView,
    UserStoryListView,
)
from . import views

urlpatterns = [
    path('', StoryListView.as_view(), name='stories-home'),
    path('story/<int:pk>', StoryDetailView.as_view(), name='story-detail'),
    path('story/new/', StoryCreateView.as_view(), name='story-create'),
    path('story/<int:pk>/update/', StoryUpdateView.as_view(), name='story-update'),
    path('story/<int:pk>/delete/', StoryDeleteView.as_view(), name='story-delete'),
    path('user/<str:username>', UserStoryListView.as_view(), name='user-stories'),
    path('about/',views.about, name='stories-about'),
]