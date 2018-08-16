from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def regex(request):
    return render(request, 'note/regex.html')


def linux(request):
    return render(request, 'note/linux.html')


def git(request):
    return render(request, 'note/git.html')
