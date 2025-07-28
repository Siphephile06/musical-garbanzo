from django.urls import path
from .views import (
    sticky_list,
    sticky_detail,
    sticky_create,
    sticky_update,
    sticky_delete
)

urlpatterns = [ 
    # URl pattern for displaying a list of sticky notes
    path('', sticky_list, name='sticky_list'),

    # URL pattern for displaying a single sticky note
    path('note/<int:pk>/', sticky_detail, name='sticky_detail'),

    # URL pattern for creating a new sticky note
    path('note/create/', sticky_create, name='sticky_create'),

    # URL pattern for updating an existing sticky note
    path('note/update/<int:pk>/', sticky_update, name='sticky_update'),

    # URL pattern for deleting a sticky note
    path('note/delete/<int:pk>/', sticky_delete, name='sticky_delete'),
]