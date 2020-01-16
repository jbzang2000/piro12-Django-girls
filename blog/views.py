from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm


# models 파일에 정의된 모델(Post)가져오기.
# get object or 404 : pk에 해당하는 Post 없으면 page404를 출력하겠다는 것


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts
    })

# 이 함수는 요청(request)을 넘겨받아 render메서드를 호출합니다.
# 이 함수는 render 메서드를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.
# posts 라는 변수 = 쿼리셋. 생성된 날짜에 따라 Post의 인스턴스를 필터한 것.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post
    })

# request와 pk를 인자로 받음. get에서 pk가 pk인 값을 찾고 없으면 404.
# 요청 받으면 저 html 반환함.

def post_new(request):
    if request.method == "POST":  # method 가 POST 면 form 에서 받은 데이터를 PostForm 으로 넘기라는 뜻.
        form = PostForm(request.POST) # 폼에서 받은 데이터를 PostForm 으로 넘겨주자
        if form.is_valid():
            post = form.save(commit=False) # form에다 save 메소드로 저장하고, 그걸 post 라고 했지
            post.author = request.user # post 의 autohr 속성을 request.user로 맞추고
            post.published_date = timezone.now() # 업로드 데이트도 맞추고
            post.save() # 변경사항을 유지할 것!
            return redirect('post_detail', pk=post.pk) # save 누르면 작성한 페이지로 이동(리턴)하게 됨.
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form': form
    })
# 여기 request 에는 내가 new 에서 쓴 정보가 담겨있다. method 가 POST 이기 때문이니까.

def post_edit(request, pk): # URL 에서 매개변수로 pk를 받는다는 차이,
    post = get_object_or_404(Post, pk=pk) # get 으로 post 호출해서 원래 글의 내용을 인스턴스로 받음
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {
        'form': form
    })



# Create your views here.
