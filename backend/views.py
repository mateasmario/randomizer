import random as rand

from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def index_view(request):
    if request.method == "POST":
        context = {}

        items = request.POST['items']
        count = request.POST['count']

        lst = items.split('\n')
        if int(count) > len(lst):
            messages.add_message(request, messages.ERROR, "You are trying to extract more elements than provided.")
            return redirect('/')

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

        return render(request, "randomized.html", context)
    else:
        return render(request, "index.html")