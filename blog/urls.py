from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post -> URL이 post 문자 포함해야 한다는 뜻
    # int:pk -> pk 라는 변수를 정수로 view에 전송한다
    # http://127.0.0.1:8000/post/5/ 라고 치면 pk로에서 5에 해당하는 값을 찾아 뷰로 전달함.
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),

]