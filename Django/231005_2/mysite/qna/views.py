from django.shortcuts import render
from django.http import HttpResponse

db = {
    1:{
        'title': '제목1',
        'contents': '내용1',
    },
    2:{
        'title': '제목2',
        'contents': '내용2',
    },
    3:{
        'title': '제목3',
        'contents': '내용3',
    },
    4:{
        'title': '제목4',
        'contents': '내용4',
    },
    5:{
        'title': '제목5',
        'contents': '내용5',
    },
}

def index(request):
    return render(request, 'qna/index.html', {'qna': db})

def qna(request, pk):
    if db.get(pk):
        return render(request, 'qna/qna.html', {'no': pk, 'qna': db.get(pk)})
    else:
        return HttpResponse('잘못된 접근입니다.')