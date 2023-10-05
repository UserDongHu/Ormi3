from django.shortcuts import render

def index(request):
    return render(request, 'notice/index.html')

def free(request):
    return render(request, 'notice/free.html')

def freedetail(request, pk):
    return render(request, 'notice/freedetail.html', {'no': pk})

def oneone(request):
    return render(request, 'notice/oneone.html')

def oneonedetail(request, pk):
    return render(request, 'notice/oneonedetail.html', {'no': pk})