# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<a target="_blank" href="https://youtube.com/"> My website</a>''')
#
# def about(request):
#     return HttpResponse("About Akash")
# ------------------------------
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>Home</h1>
    # <a target = "_blank" href="http://127.0.0.1:8000/removepunc"> Remove Punctuation </a>''')
def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    # check which operation is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charactercounter == "on":
        analyzed = "Total counted words are: " + str(len(djtext))
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        djtext = analyzed
    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on":
        return HttpResponse("Please select any operation for the manipulation")

    return render(request, 'analyze.html', params)
