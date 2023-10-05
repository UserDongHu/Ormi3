from django.shortcuts import render

db = {
    1 : {
        'name': '상품1',
        'price': 5000,
    },
    2 : {
        'name': '상품2',
        'price': 5000,
    },
    3 : {
        'name': '상품3',
        'price': 5000,
    },
    4 : {
        'name': '상품4',
        'price': 5000,
    },
    5 : {
        'name': '상품5',
        'price': 5000,
    },
    6 : {
        'name': '상품6',
        'price': 5000,
    },
    7 : {
        'name': '상품7',
        'price': 5000,
    },
    8 : {
        'name': '상품8',
        'price': 5000,
    },
    9 : {
        'name': '상품9',
        'price': 5000,
    },
    10 : {
        'name': '상품10',
        'price': 5000,
    },
}

def index(request):
    return render(request, 'main/index.html', {'product': db})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')