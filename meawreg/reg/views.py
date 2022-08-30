from django.shortcuts import render

from .models import Subject

# Create your views here.

def index(request):
    subjects_list = Subject.objects.all()
    return render(request, 'subject_list/index.html', {
        'subject_list' : subjects_list
    })
    