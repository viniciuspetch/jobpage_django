from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Candidate
from .forms import CandidateForm

def index(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('website:index'))
    else:
        candidate_list = Candidate.objects.all()
        form = CandidateForm(initial={
            'full_name': "Someone",
            'email': "me@you.com",
            'phone': "123456789",
            'pres_letter': "Nothing to say",
            'linkedin_link': "http://linkedin.com",
            'github_link': "http://github.com",
            'eng_level': 123,
            'salary': 123,
        })
        context = {
            'candidate_list': candidate_list,
            'form': form,
        }
    return render(request, 'website/index.html', context)

def send(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('website:index'))
    
    