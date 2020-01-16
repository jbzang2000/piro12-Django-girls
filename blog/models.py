from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #장고 모델이라는 거를 상속받았군.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#이걸 호출하면 제목 텍스트를 얻게 굄. return self.title 이니까.
        return self.title