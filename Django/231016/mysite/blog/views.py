from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

class PostList(ListView):
    model = Post
    ordering = '-pk'
    
    def get_queryset(self):
        queryset = super().get_queryset() # ListView의 get_queryset메서드를 사용. Post 모델의 전체 객체 목록을 반환
        
        # request의 GET 파라미터에서 'q'를 가져옵니다.
        q = self.request.GET.get('q', '')
        
        # 'q' 파라미터가 제공되었을 경우, 쿼리셋을 필터링함
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return queryset
    
class PostDetail(DetailView):
    model = Post
    
class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')
    
class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('postlist')
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')
    
class PostTest(CreateView):
    model = Post
    
    def get(self, request):
        return HttpResponse('PostTest get')
    
    def post(self, request):
        return HttpResponse('PostTest post')
    
postlist = PostList.as_view() # as_view는 진입 메소드
postdetail = PostDetail.as_view()
write = PostCreate.as_view()
edit = PostUpdate.as_view()
delete = PostDelete.as_view()
test = PostTest.as_view()
