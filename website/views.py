from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Candidate
from .forms import CandidateForm

def index(request):
    candidate_list = Candidate.objects.all()
    form = CandidateForm()
    context = {
        'candidate_list': candidate_list,
        'form': form,
    }
    return render(request, 'website/index.html', context)

def send(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('website:index'))
    else:
        form = CandidateForm()
    context = {
        'form': form,
    }
    return render(request, 'website/index.html', context)
    
    