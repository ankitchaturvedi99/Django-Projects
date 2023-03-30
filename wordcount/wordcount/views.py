from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist=fulltext.split()
    worddictonary = {}

    for word in wordlist:
        if word in worddictonary:
            #Increase
            worddictonary[word]+=1
        else:
            #addto the dictonary
            worddictonary[word] = 1


    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictonary':worddictonary.items()})
   