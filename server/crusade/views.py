from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello world")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
