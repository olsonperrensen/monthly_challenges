from calendar import month
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def index(req):
    return HttpResponse("<pre>Welcome to the challenges index page.</pre>")


def monthly_challenge_num(req, maand):
    return HttpResponse(maand)


def monthly_challenge(request, maand):
    monthly_challenges = {
        "jan": "Eat no meat for an entire month!",
        "feb": "Walk for at least 20 minutes every day!",
        "mar": "Learn Django for at least 20 minutes every day!",
        "apr": "Swim for 15 minutes in hot water!",
        "may": "Practice mindfulness five times a week",
        "jun": "Play with your dogs in the evening",
        "jul": "Contemplate your achievments",
        "aug": "Sing mantras with a group of people each day",
        "sep": "Improve your poetry skills 1 hour a month",
        "oct": "Learn Chinese 5 minutes a day",
        "nov": "Do yoga at a gym for 45 minutes",
        "dec": "Write a journal before going to sleep every day in between",
    }
    try:
        return HttpResponse(monthly_challenges[maand])
    except:
        return HttpResponseNotFound('This month is not supported yet!')
