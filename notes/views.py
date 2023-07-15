from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import DetailView, ListView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = "notes/note_detail.html"


# def list(request):
#     all_notes = Notes.objects.all()

#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Notes does not exist')
#     return render(request, 'notes/note_detail.html',{'note':note})
