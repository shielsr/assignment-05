from django import forms
from .models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content', 'number']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }