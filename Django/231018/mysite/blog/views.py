from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# rest_framework 추가 후 추가된 코드
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import PostSerializer

# def postlist(request):
#     posts = [
#         {'title':'1', 'content':'111'},
#         {'title':'2', 'content':'222'},
#         {'title':'3', 'content':'333'},
#     ]
#     return JsonResponse(posts, safe=False) # 딕셔너리 이외를 받을 경우, safe=False로 설정

# FBV 사용하는 방식
# @api_view(['GET']) # ['GET', 'POST'] 하면 둘다 처리 가능
# def postlist(request):
#     posts = [
#         {'title':'1', 'content':'111'},
#         {'title':'2', 'content':'222'},
#         {'title':'3', 'content':'333'},
#     ]
#     serializer = posts # 직렬화 하는 단계
#     return Response(serializer) # Response로 반환되었을 때 데이터를 읽을 수도 있고, POST를 보낼 수도 있음.

# CBV 사용하는 방식
# class LicatView(APIView):
#     def get(self, request):
#         posts = [
#             {'title':'1', 'content':'111'},
#             {'title':'2', 'content':'222'},
#             {'title':'3', 'content':'333'},
#         ]
#         serializer = posts # 직렬화 하는 단계
#         return Response(serializer) # Response로 반환 되었을 때 데이터를 읽을 수도 있고, POST를 보낼 수도 있습니다.
# postlist = LicatView.as_view()


# @api_view(['GET', 'POST'])
# def postlist(request):
#     if request.method == 'GET':
#         postlist = Post.objects.all()
#         serializer = PostSerializer(postlist, many=True) # 다수의 Queryset을 넘길 때 many=True
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(APIView):
    def get(self, request, format=None):
        postlist = Post.objects.all()
        serializer = PostSerializer(postlist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
postlist = PostList.as_view()