from django.shortcuts import render

def index(request, pk=0):
    return render(request, 'main/index.html', {'no': pk})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
