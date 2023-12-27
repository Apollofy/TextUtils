# I have created this website
from django.http import HttpResponse

from django.shortcuts import render
def index(request):
        return render(request,'index.html')


def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')

    # Check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover =request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')

    # Check which textbox is on
    if (removepunc == "on"):
        punctutations='''.,?!:;--[]{}()'"...'''
        analyzed = ""
        for char in djtext:
            if char not in punctutations:
                    analyzed = analyzed +char
        params= {'purpose': 'Removed Punctutations','analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in  djtext:
            analyzed = analyzed + char.upper()
        params= {'purpose': 'Change to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in  djtext:
            if char !="\n" and char!="\r":
                 analyzed = analyzed + char
            params= {'purpose': 'Remove the newline character','analyzed_text':analyzed}
        djtext=analyzed
    if(spaceremover=="on"):
        analyzed=""
        for char in djtext:
            if char!=" ":
                analyzed = analyzed + char
            params= {'purpose': 'Remove the space','analyzed_text':analyzed}
    
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on"):
         return HttpResponse("error")
    return render(request,'analyze.html',params)
                   