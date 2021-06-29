from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'poll/home.html', context)


def create(request):
    context = {}
    return render(request, 'poll/create.html', context)


def result(request, poll_id):
    context = {}
    return render(request, 'poll/result.html', context)


def vote(request, poll_id):
    context = {}
    return render(request, 'poll/vote.html', context)
