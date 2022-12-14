from ast import arg
from calendar import month
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

# Create your views here.
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
    "dec": None,
}


def index(req):
    months = list(monthly_challenges.keys())
    return render(req, "challenges/index.html", {
        "mMonths": months
    })


def monthly_challenge_num(req, nr):
    m = list(monthly_challenges.keys())
    if nr < len(m) and nr != 0:
        redirect_month = m[nr-1]
        redi = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redi)
    else:
        return HttpResponseNotFound("Invalid month man.")


def monthly_challenge(request, maand):
    try:
        challenge_text = monthly_challenges[maand]
        return render(request, "challenges/challenge.html", {
            "mText": challenge_text,
            "mMonth": maand
        })
    except:
        raise Http404()
