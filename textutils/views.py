#I(AYAN KHAN) have created the web page


from django.http import HttpResponse    
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext= request.POST.get('text','default')
    # print(djtext)
    #check box value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')

    # logic
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
      
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcaps=="on"):
     analyzed = ""
     for char in djtext:
        analyzed = analyzed + char.upper()
    
     params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed }
     djtext = analyzed
    #  return render(request, 'analyze.html', params)
     
    if(newlineremove =="on"):
       analyzed = ""
       for char in djtext:
          if char !="\n" and char != "\r":
             analyzed = analyzed + char
       params = {'purpose':'newlineremove', 'analyzed_text': analyzed }
       djtext = analyzed
    #    return render(request, 'analyze.html', params)
    
    if(spaceremove =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if index < len(djtext) - 1 and djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose':'spaceremove', 'analyzed_text': analyzed }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if(charcount =="on"):
    #  analyzed = len(djtext)
    
    #  logic witout the predefined method 
     analyzed = 0
     for char in djtext:
        if char == " ":
           pass
        else:
         analyzed += 1

     params = {'purpose':'Count of text', 'analyzed_text': analyzed }
     djtext = analyzed
    #  return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps !="on" and charcount !="on" and spaceremove !="on" and newlineremove !="on") :
         return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)

     

 



































