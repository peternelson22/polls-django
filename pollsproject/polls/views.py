from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    questions = Question.objects.all().order_by('-pub_date')
    context = {'questions': questions}
    return render(request, 'index.html', context)

def detail(request, pk):
    try:
        question = Question.objects.get(id=pk)
    except Question.DoesNotExist:
        raise Http404('Question does exist')

    return render(request, 'detail.html', {'question': question})

def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'results.html', {'question': question})

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST.get('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': "You didn't select a choice."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
