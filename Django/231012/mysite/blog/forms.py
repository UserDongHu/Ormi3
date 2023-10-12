from django import forms
from .models import Post


class PostForm(forms.ModelForm): # 모델 폼
    
    class Meta:
        model = Post
        fields = ['title', 'contents', 'main_image']