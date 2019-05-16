from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    POINT = (
        (1, '♥'),
        (2, '♥♥'),
        (3, '♥♥♥'),
        (4, '♥♥♥♥'),
        (5, '♥♥♥♥♥'),
    )

    title = models.CharField(max_length=200)
    img = models.FileField(null=True)
    price = models.IntegerField()
    point = models.IntegerField(choices=POINT, default=3)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, default = "")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', default=0)
    user = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
