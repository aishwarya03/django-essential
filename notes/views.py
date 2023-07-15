from django.shortcuts import render
from .models import Notes
from django.http import Http404

# Create your views here.

def list(request):
    all_notes = Notes.objects.all()

    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404('Notes does not exist')
    return render(request, 'notes/note_detail.html',{'note':note})
