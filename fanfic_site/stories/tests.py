from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Story

class StoryModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.story = Story.objects.create(
            title='Test Story',
            author=cls.user,
            summary='This is a test story',
            fandom='Indiana Jones',
        )
        
    def test_story_content(self):
        story = Story.objects.get(id=1)
        expected_title = f'{story.title}'
        expected_author = f'{story.author}'
        expected_summary = f'{story.summary}'
        expected_fandom = f'{story.fandom}'
        expected_genre = f'{story.fandom}'
        self.assertEqual(expected_title, 'Test Story')
        self.assertEqual(expected_author, 'testuser')
        self.assertEqual(expected_summary, 'This is a test story')
        self.assertEqual(expected_fandom, 'Indiana Jones')
        
        
    def test_story_str_method(self):
        story = Story.objects.get(id=1)
        self.assertEqual(str(story), story.title)
        
    def test_get_absolute_url(self):
        story = Story.objects.get(id=1)
        self.assertEqual(story.get_absolute_url(), reverse('story-detail', args=[story.id]))