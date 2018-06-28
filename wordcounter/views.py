from django.http import HttpRequest
from django.shortcuts import render
import operator

def index(request):
    return render(request, 'index.html', {'name' : 'nitin suryawanshi'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordnumber = {}
    for word in wordlist:
        if word in wordnumber:
            wordnumber[word] += 1

        else:
            wordnumber[word] = 1

    shortedword = sorted(wordnumber.items(), key=operator.itemgetter(1))

    return render (request, 'count.html', {'fulltext':fulltext, 'wordlist' :len(wordlist), 'shortedword':shortedword  })

def About(request):
    return render (request, 'about.html')
