from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from .models import Story, Chapter
from .forms import ChapterForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

User = get_user_model()

class StoryListView(ListView):
    model = Story
    template_name = 'stories/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'stories'
    ordering = ['-date_published']
    paginate_by = 4
    
    def get_queryset(self):
        return Story.objects.filter(status='published').order_by('-date_published')
    
class UserStoryListView(ListView):
    model = Story
    template_name = 'stories/user_stories.html'
    context_object_name = 'stories'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
    
        if self.request.user == user:
            # Author sees everything
            return user.stories.all().order_by('-date_published')
        else:
            # Others see only published stories
            return user.stories.filter(status='published').order_by('-date_published')

class StoryDetailView(DetailView):
    model = Story
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = self.object.chapters.all()
        context['title'] = self.object.title
        return context

class ChapterDetailView(DetailView):
    model = Chapter
    template_name = "stories/chapter_detail.html"

    def get_object(self):
        story_id = self.kwargs["story_id"]
        number = self.kwargs["number"]

        return get_object_or_404(
            Chapter,
            story_id=story_id,
            number=number
        )
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.story.title} - Chapter {self.object.number}: {self.object.title}"
        return context
        
class UpdateChapter(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'stories/add_chapter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = self.object.story
        return context

    def get_success_url(self):
        return redirect('chapter-detail', story_id=self.object.story.id, number=self.object.number).url

    def test_func(self):
        chapter = self.get_object()
        return self.request.user == chapter.story.author


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'genre', 'summary', 'cover_image']   
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        form.instance.status = 'draft' 
        return super().form_valid(form) # Validate the form by running form_valid method from the parent class
    
@login_required
def TogglePublish(request, pk):
    story = get_object_or_404(Story, pk=pk, author=request.user)

    if story.status == 'draft':
        story.status = 'published'
        # Only set date_published if it was never published before
        if not story.date_published or story.date_published == story._meta.get_field('date_published').default:
            story.date_published = timezone.now()
    elif story.status == 'published':
        story.status = 'draft'

    # Optionally, leave hiatus stories unchanged
    story.save()

    return redirect('story-detail', pk=story.pk)

class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ['title', 'genre', 'status', 'summary', 'cover_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        story = self.get_object()
        return self.request.user == story.author
    
class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # New class PostDeleteView created here
    model = Story
    success_url = "/"

    def test_func(self):
        story = self.get_object()
        return self.request.user == story.author

def about(request):
    return render(request, 'stories/about.html', {'title': 'About'})


class AddChapter(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'stories/add_chapter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = get_object_or_404(Story, id=self.kwargs['story_id'])
        return context

    def form_valid(self, form):
        story = get_object_or_404(Story, id=self.kwargs['story_id'])
        form.instance.story = story
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form errors:", form.errors)  # Add this line
        return super().form_invalid(form)

    def get_initial(self):
        story = get_object_or_404(Story, id=self.kwargs['story_id'])
        return {'number': story.chapters.count() + 1}

    def get_success_url(self):
        return redirect('chapter-detail', story_id=self.object.story.id, number=self.object.number).url

    def test_func(self):
        story = get_object_or_404(Story, id=self.kwargs['story_id'])
        return self.request.user == story.author
    
@login_required
@require_POST
def reorder_chapters(request, pk):
    story = get_object_or_404(Story, pk=pk)
    
    # Check if user is the author
    if request.user != story.author:
        return JsonResponse({'success': False, 'error': 'Permission denied'}, status=403)
    
    try:
        data = json.loads(request.body)
        chapters = data.get('chapters', [])
        
        # First, set all chapters to high temporary numbers (1000+) to avoid conflicts
        for i, chapter_data in enumerate(chapters):
            chapter = Chapter.objects.get(id=chapter_data['id'], story=story)
            chapter.number = 1000 + i
            chapter.save()
        
        # Then, update to the actual new numbers
        for chapter_data in chapters:
            chapter = Chapter.objects.get(id=chapter_data['id'], story=story)
            chapter.number = chapter_data['number']
            chapter.save()
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)