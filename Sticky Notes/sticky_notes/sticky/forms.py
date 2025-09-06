from django import forms
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    '''Form for creating and updating sticky notes.

    Fields:
        title (str): The title of the sticky note.
        content (str): The content of the sticky note.
        color_tag (str): The color tag of the sticky note.
    '''
    class Meta:
        model = StickyNote
        fields = ['title', 'content', 'color_tag']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Content'}),
            'color_tag': forms.Select(choices=[
                ('yellow', 'Yellow'),
                ('blue', 'Blue'),
                ('green', 'Green'),
                ('pink', 'Pink'),
                ('red', 'Red')
            ]),
        }
