from django.urls import path
from .views import (
    StoryListView,
    StoryDetailView,
    StoryCreateView,
    StoryUpdateView,
    StoryDeleteView,
    UserStoryListView,
    ChapterDetailView,
    AddChapter,
    UpdateChapter,
    TogglePublish,
    reorder_chapters,
)
from . import views


urlpatterns = [
    path("", StoryListView.as_view(), name="stories-home"),
    path("story/<int:pk>", StoryDetailView.as_view(), name="story-detail"),
    path("story/new/", StoryCreateView.as_view(), name="story-create"),
    path("story/<int:pk>/update/", StoryUpdateView.as_view(), name="story-update"),
    path("story/<int:pk>/delete/", StoryDeleteView.as_view(), name="story-delete"),
    path("user/<str:username>", UserStoryListView.as_view(), name="user-stories"),
    path("about/", views.about, name="stories-about"),
    path("<int:pk>/", StoryDetailView.as_view(), name="story-detail"),
    path(
        "<int:story_id>/chapters/<int:number>/",
        ChapterDetailView.as_view(),
        name="chapter-detail",
    ),
    path("<int:story_id>/add-chapter/", AddChapter.as_view(), name="add-chapter"),
    path(
        "<int:story_id>/chapter/<int:pk>/update/",
        UpdateChapter.as_view(),
        name="chapter-update",
    ),
    path("story/<int:pk>/reorder-chapters/", reorder_chapters, name="reorder-chapters"),
    path("story/<int:pk>/toggle/", TogglePublish, name="story-toggle"),
]
