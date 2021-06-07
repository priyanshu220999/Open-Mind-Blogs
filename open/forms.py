from django import forms
from open.models import Story,Review

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':
                                         'editable medium-editor-textarea storycontent'}),
        }

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('author','text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':
                                              'editable medium-editor-textarea storycontent'}),
        }
