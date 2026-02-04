from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Story, Genre

class StoryModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.genre = Genre.objects.create(name='Fantasy')
        cls.story = Story.objects.create(
            title='Test Story',
            author=cls.user,
            summary='This is a test story',
            fandom='Indiana Jones',
            genre=cls.genre,
            status='draft'
        )


    def test_story_content(self):
        story = Story.objects.get(id=1)
        expected_title = f'{story.title}'
        expected_author = f'{story.author}'
        expected_summary = f'{story.summary}'
        expected_fandom = f'{story.fandom}'
        expected_genre = f'{story.genre}'
        expected_status = f'{story.status}'
        self.assertEqual(expected_title, 'Test Story')
        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_summary, 'This is a test story')
        self.assertEqual(expected_fandom, 'Indiana Jones')
        self.assertEqual(expected_genre, 'Fantasy')
        self.assertEqual(expected_status, 'draft')
        
        
    def test_story_str_method(self):
        story = Story.objects.get(id=1)
        self.assertEqual(str(story), story.title)
        
    def test_get_absolute_url(self):
        story = Story.objects.get(id=1)
        self.assertEqual(story.get_absolute_url(), reverse('story-detail', args=[story.id]))
        
    def test_story_date_published_default(self):
        """Test that date_published is set by default"""
        self.assertIsNotNone(self.story.date_published)
        self.assertIsInstance(self.story.date_published, timezone.datetime)
        
        
class StoryViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.story = Story.objects.create(
            author=self.user,
            title='Test Story',
            summary='This is a test story',
            status='published'
        )
        
    def test_stories_list_view(self):
        url = reverse('stories-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test story')
        self.assertTemplateUsed(response, 'stories/home.html')
        
    def test_story_detail_view(self):
        url = reverse('story-detail', args=[self.story.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.story.title)
        
        def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

        response = self.client.post(reverse('post-create'), {
            'title': 'New title',
            'content': 'New text',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        self.assertTrue(Post.objects.filter(title='New title').exists())
        
        
     def test_create_post_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

        response = self.client.post(reverse('post-create'), {
            'title': 'New title',
            'content': 'New text',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        self.assertTrue(Post.objects.filter(title='New title').exists())