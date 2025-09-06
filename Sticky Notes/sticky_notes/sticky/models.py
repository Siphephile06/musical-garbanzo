from django.db import models


class StickyNote(models.Model):
    '''Model representing a sticky note.

    Fields:
        title (str): The title of the sticky note.
        content (str): The content of the sticky note.
        color_tag (str): The color tag of the sticky note, default is 'yellow'.
        created_at (datetime): The date and time when the sticky note was
            created.
        updated_at (datetime): The date and time when the sticky note was last
            updated.
    Relations:
        topic (ForeignKey): The topic to which the sticky note belongs.

    Methods:
        __str__(): Returns a string representation of the sticky note.
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    color_tag = models.CharField(max_length=20, default='yellow', choices=[
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('pink', 'Pink'),
        ('red', 'Red')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Define a foreign key for the topic's relationship
    topic = models.ForeignKey(
                                'Topic', on_delete=models.CASCADE, null=True,
                                blank=True
                                )

    def __str__(self):
        return self.title


class Topic(models.Model):
    '''Model representing a topic for sticky notes.
    Fields:
        name (str): The name of the topic.
    Methods:
        __str__(): Returns a string representation of the topic.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
