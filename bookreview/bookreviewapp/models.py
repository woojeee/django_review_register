from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    POINT = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    point = models.IntegerField(choices=POINT)
    contents = models.TextField()  
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
