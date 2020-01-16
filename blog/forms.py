from django import forms
from .models import Post

class PostForm(forms.ModelForm):
   # 우리가 만들 폼 이름이고 이게 ModelForm 이라는걸 상속받음
    class Meta:
        model = Post
        # 만들 품이 어떤 model 인지(Post 쓰지)
        fields = {
            'title',
            'text',
        }