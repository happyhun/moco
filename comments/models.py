from django.db import models
from users.models import User
from posts.models import Post
from place.models import Place

# Create your models here.


class Comment(models.Model):
    TAG_POST = 1
    TAG_PLACE = 2
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.IntegerField()  # 1이면 post, 2면 place
    content = models.TextField()
    cmt_class = models.IntegerField(default=0)
