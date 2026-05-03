from django.db import models


class Memo(models.Model):
    content = models.TextField(max_length=100)  # 문자열 타입의 content 필드
    created_at = models.DateTimeField(auto_now_add=True)  # 날짜 타입의 created_at 필드

    def __str__(self):
        return self.content
