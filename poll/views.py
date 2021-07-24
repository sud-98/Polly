from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Poll
from .forms import CreatePoll
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'poll/home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePoll(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Poll Created Successfully! Vote Now'
            )
            return redirect('poll-home')
    else:
        form = CreatePoll()
    context = {
        'form': form
    }
    return render(request, 'poll/create.html', context)


def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/result.html', context)


@login_required
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        sel_option = request.POST['poll']

        if sel_option == 'option1':
            poll.option1_count += 1
        elif sel_option == 'option2':
            poll.option2_count += 1
        elif sel_option == 'option3':
            poll.option3_count += 1
        else:
            return HttpResponse(400, 'Invalid Option')

        poll.save()
        return redirect('poll-result', poll.id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)
