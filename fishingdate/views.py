from django.shortcuts import render
from .models import Notebook

def notebook_view(request):
    notebook = Notebook.objects.get(id=1)
    return render(request, 'notebook.html', {'notebook': notebook})
