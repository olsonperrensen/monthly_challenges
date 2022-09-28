from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(req):
    return HttpResponse("<pre>Welcome to the challenges index page.</pre>")

def monthly_challenge_num(req,maand):
    challenge = None
    if maand == 1:
        challenge = '1Eat no meat for an entire month!'
    elif maand == 2:
        challenge = '2Walk for at least 20 minutes every day!'
    elif maand == 3:
        challenge = '3Learn Django for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound('0 This month is not supported yet!')
    return HttpResponse(challenge)

def monthly_challenge(request, maand):
    challenge = None
    if maand == 'january':
        challenge = 'Eat no meat for an entire month!'
    elif maand == 'february':
        challenge = 'Walk for at least 20 minutes every day!'
    elif maand == 'march':
        challenge = 'Learn Django for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound('This month is not supported yet!')
    return HttpResponse(challenge)
