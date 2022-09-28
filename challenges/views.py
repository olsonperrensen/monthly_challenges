from ast import arg
from calendar import month
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "dec": "Write a journal before going to sleep every day in between",
}


def index(req):
    html_res = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <style>
        a
        {
            color: orange;
            font-size: 26px;
            margin: 50%;
        }
        ul
        {
                        padding: 6px;
        }
    </style>
'''
    for k in monthly_challenges.keys():
        html_res += f"<ul><a href='{reverse('month-challenge', args=[k])}'>{k}</a></ul>"
    return HttpResponse(html_res)


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
        return HttpResponse(monthly_challenges[maand])
    except:
        return HttpResponseNotFound('This month is not supported yet!')
