from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from .models import Story
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