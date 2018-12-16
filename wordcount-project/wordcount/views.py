from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('<h1>Hello!<h1>')
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word]+=1

            #increase
        else:
            #add to the word_dictionary
            word_dictionary[word]=1
    sortedWords=sorted(word_dictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedWords':sortedWords})
