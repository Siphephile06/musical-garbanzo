from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote 
from .forms import StickyNoteForm


def sticky_list(request):
    '''View to list all sticky notes.

    Returns:
        Rendered template with the list of sticky notes.
    '''
    notes = StickyNote.objects.all()
    return render(request, 'sticky/sticky_list.html', {'notes': notes})


def sticky_detail(request, pk):
    '''View to display a single sticky note.

    Args:
        pk (int): Primary key of the sticky note.

    Returns:
        Rendered template with the sticky note details.
    '''
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'sticky/sticky_detail.html', {'note': note})


def sticky_create(request):
    '''View to create a new sticky note.

    Returns:
        Rendered template with the form for creating a sticky note.
    '''
    form = StickyNoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('sticky_list')
    return render(request, 'sticky/sticky_form.html', {'form': form})


def sticky_update(request, pk):
    '''View to update an existing sticky note.

    Args:
        pk (int): Primary key of the sticky note to update.

    Returns:
        Rendered template with the form for updating the sticky note.
    '''
    sticky = get_object_or_404(StickyNote, pk=pk)
    form = StickyNoteForm(request.POST or None, instance=sticky)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('sticky_detail', pk=sticky.pk)
    return render(request, 'sticky/sticky_form.html', {'form': form})


def sticky_delete(request, pk):
    '''View to delete a sticky note.

    Args:
        pk (int): Primary key of the sticky note to delete.

    Returns:
        Redirects to the sticky list after deletion.
    '''
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('sticky_list')

    return render(request, 'sticky/sticky_confirm_delete.html', {'note': note})