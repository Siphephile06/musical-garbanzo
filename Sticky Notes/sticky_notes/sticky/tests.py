from django.test import TestCase
from django.urls import reverse 
from .models import StickyNote, Topic


class StickyNoteModelTest(TestCase):
    def setUp(self):
        # Create a topic and a sticky note for testing
        self.topic = Topic.objects.create(name='Test Topic')
        self.sticky_note = StickyNote.objects.create(
            title='Test Note',
            content='This is a test note.',
            color_tag='yellow',
            topic=self.topic
        )

    def test_StickyNote_has_title(self):
        self.assertEqual(self.sticky_note.title, 'Test Note')

    def test_StickyNote_has_content(self):
        self.assertEqual(self.sticky_note.content, 'This is a test note.')
    
    def test_StickyNote_has_color_tag(self):
        self.assertEqual(self.sticky_note.color_tag, 'yellow')


class StickyNoteViewsTest(TestCase):
    def setUp(self):
        # Create a topic and a sticky note for testing
        self.topic = Topic.objects.create(name='Test Topic')
        self.sticky_note = StickyNote.objects.create(
            title='Test Note',
            content='This is a test note.',
            color_tag='yellow',
            topic=self.topic
        )
        url = reverse('sticky_delete', kwargs=[{'pk': self.sticky_note.id}])

    def test_sticky_list_view(self):
        response = self.client.get(reverse('sticky_list', 
                                           ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_sticky_detail_view(self):
        response = self.client.get(reverse('sticky_detail', 
                                           args=[self.sticky_note.id]
                                           ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test note.')

    def test_sticky_create_view(self):
        response = self.client.get(reverse('sticky_create',
                                           ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create StickyNote')

    def test_sticky_update_view(self):
        response = self.client.get(reverse('sticky_update', 
                                           reverse('sticky_update', 
                                                   kwargs=[
                                                       {'pk': 
                                                        self.sticky_note.id}
                                                       ]
                                                         ))
                                           )
                                               
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update StickyNote')

    def test_sticky_delete_view(self):
        response = self.client.get(reverse('sticky_delete', 
                                           args=[self.sticky_note.id]
                                           ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete StickyNote')


