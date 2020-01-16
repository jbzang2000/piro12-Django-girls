"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    #import include : 내가 blog
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #이걸 추가함! 메인 주소로 들어오는 모든 접속 요청을 blog.urls로 전송해서 추가 명령을 찾을 거다.
    #이렇게 하면 이 파일에서 urls 처리하는게 아니라 blog로 뭐가 들어가고 그걸 여기서 불러오겠지.
]