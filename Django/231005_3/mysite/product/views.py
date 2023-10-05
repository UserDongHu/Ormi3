from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import re

mykeyword = 'apple' # 검색하고싶은 키워드
res = requests.get(f'https://www.fmkorea.com/search.php?mid=hotdeal&category=1196845148&listStyle=webzine&search_keyword={mykeyword}&search_target=title') # 가전제품 카테고리에서 제목 검색
res.raise_for_status() # 200(정상)이 아니면 오류 발생

html = res.text
soup = BeautifulSoup(html, 'html.parser')

productDB = {}
productcount = 0

productlist = soup.select('#content>.content_dummy>div>div>div>ul>li')

for container in productlist:
    productcount += 1

    title = container.select('.title a')[0].text.strip()
    title = re.sub(r'\t|\xa0|\[\d+\]', '', title)

    price = container.select('.hotdeal_info>span')[1].select('.strong')[0].text

    productDB[productcount] = {'title': title, 'price': price}

def index(request):
    return render(request, 'product/index.html', {'productDB': productDB})

def product(request, pk):
    if productDB.get(pk):
        return render(request, 'product/product.html', {'no': pk, 'product': productDB.get(pk)})
    else:
        return HttpResponse('잘못된 접근입니다.')