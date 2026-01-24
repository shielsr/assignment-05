from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Story, Chapter
from .forms import ChapterForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


User = get_user_model()

class StoryListView(ListView):
    model = Story
    template_name = 'stories/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'stories'
    ordering = ['-date_published']
    paginate_by = 4
    
class UserStoryListView(ListView):
    model = Story
    template_name = 'stories/user_stories.html'
    context_object_name = 'stories'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user.stories.order_by('-date_published')

class StoryDetailView(DetailView):
    model = Story
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = self.object.chapters.all()
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

class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'content']    
    
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate the form by running form_valid method from the parent class

class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ['title', 'content']

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


def AddChapter(request, story_id):
    story = get_object_or_404(Story, id=story_id)

    # Optional: check if current user is author
    if request.user != story.author:
        return render(request, 'stories/forbidden.html', status=403)

    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.story = story
            chapter.save()
            return redirect('chapter-detail', story_id=story.id, number=chapter.number)
    else:
        # Suggest the next chapter number automatically
        next_number = story.chapters.count() + 1
        form = ChapterForm(initial={'number': next_number})

    return render(request, 'stories/add_chapter.html', {'form': form, 'story': story})