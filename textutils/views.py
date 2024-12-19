#I have created this file - Zeeshan
from django.http import HttpResponse
from django.shortcuts import render

 
def index(request):
    return render(request, 'index.html')

def ex1 (request):
    s = '''<h2>Navigation Bar <br></h2>
    <a href = "https://youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&si=K8jDiGZz6Kk1eNRD">Django with harry</a><br>
             <a href="https://www.facebook.com/"/>Facebook</a><br>
             <a href="https://www.youtube.com/"/>Youtube</a><br>
             <a href="https://g.co/kgs/rv9BrJA"/>Google</a><br>'''
    return HttpResponse(s)

def analyze(request):
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
               analyzed =analyzed + char
               

        params = {'purpose': 'Removed Punctuations','analyzed_text':
         analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase','analyzed_text':
         analyzed}
        djtext = analyzed

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines','analyzed_text':
         analyzed}
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines','analyzed_text':
         analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on") :
        return HttpResponse("Error")    
    return render(request,'analyze.html',params)