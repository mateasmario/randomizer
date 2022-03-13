import random as rand

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from backend.models import Feedback


def index_view(request):
    if request.method == "POST":
        context = {}

        items = request.POST['items']
        count = request.POST['count']

        context['previousItems'] = items
        context['previousCount'] = count

        lst = items.split('\n')
        if lst[-1] == "":
            lst.remove(lst[-1])

        if int(count) > len(lst):
            messages.add_message(request, messages.ERROR, "You are trying to extract more elements than provided.")
            return render(request, "index.html", context)

        lstProcessed = []

        for el in lst:
            if el[-1] == '\r':
                el = el[:len(el)-1]
            lstProcessed.append(el)

        count = int(count)
        context['count'] = count

        randList = []
        for i in range(count):
            pos = -1
            if len(lstProcessed) == 1:
                pos = 0
            else:
                pos = rand.randrange(0, len(lstProcessed))

            randList.append(lstProcessed[pos])
            lstProcessed.pop(pos)
            count -= 1

        context['randList'] = randList

        return render(request, "index.html", context)
    else:
        return render(request, "index.html")

def number_view(request):
    if request.method == "POST":
        context = {}

        lower = request.POST['lower']
        upper = request.POST['upper']
        count = request.POST['count']
        context['lower'] = lower
        context['upper'] = upper
        context['count'] = count

        if int(lower) >= int(upper):
            messages.add_message(request, messages.ERROR, "The lower bounds should be strictly smaller than the upper bounds.")
            return render(request, "number.html", context)

        randList = []

        for i in range(0, int(count)):
            randList.append(rand.randrange(int(lower), int(upper)+1))

        context['randList'] = randList

        return render(request, "number.html", context)
    else:
        return render(request, "number.html")

def coin_view(request):
    if request.method == "POST":
        context = {}
        no = rand.randrange(0, 2)
        if (no == 0):
            context['result'] = 'Heads'
        else:
            context['result'] = 'Tails'
        return render(request, "coin.html", context)
    else:
        return render(request, "coin.html")

def feedback_view(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        Feedback.objects.create(name=name, message=message)
        messages.add_message(request, messages.SUCCESS, "Feedback has been sent to the website creator. Thank you!")
    return render(request, "feedback.html")